import psycopg2
from psycopg2 import sql
import configparser

class PostgreSQLConnector:

    def __init__(self, ini_file='config.ini'):
        # Read database credentials from the INI file
        self.host, self.user, self.password, self.database, self.table = self.read_database_credentials(ini_file)
        self.connection = None
        self.cursor = None

    def read_database_credentials(self, ini_file):
        # Initialize ConfigParser
        config = configparser.ConfigParser()
        # Read the INI file
        config.read(ini_file)
        # Extract database credentials
        return (
            config.get('DATABASE CREDENTIALS postgreSQL', 'host'),
            config.get('DATABASE CREDENTIALS postgreSQL', 'user'),
            config.get('DATABASE CREDENTIALS postgreSQL', 'password'),
            config.get('DATABASE CREDENTIALS postgreSQL', 'database'),
            config.get('DATABASE CREDENTIALS postgreSQL', 'table')
        )

    def connect(self):
        # Establish a database connection
        self.connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        # Disconnect from the database
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, query, data=None):
        try:
            # Connect to the database
            self.connect()
            # Execute the query with optional data
            self.cursor.execute(query, data) if data else self.cursor.execute(query)
            # Fetch and return the results
            return self.cursor.fetchall()
        except psycopg2.Error as err:
            # Handle database errors
            print(f"Error executing query: {err}")
            return None
        finally:
            # Disconnect from the database
            self.disconnect()

# Example usage
if __name__ == "__main__":
    # Create an instance of PostgreSQLConnector
    connector = PostgreSQLConnector()

    # Example query: SELECT * FROM your_table;
    table_name = connector.table
    select_query = sql.SQL("SELECT schematic_id FROM {}").format(sql.Identifier(table_name))

    # Execute the query
    results = connector.execute_query(select_query)

    # Display the results
    if results:
        for row in results:
            print(row)
