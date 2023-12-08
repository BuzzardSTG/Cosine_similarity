from datetime import datetime

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