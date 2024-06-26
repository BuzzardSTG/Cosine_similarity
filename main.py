from psycopg2 import sql
from connector_postgre import PostgreSQLConnector
from connector_mysql import MySQLConnector
import time
import datetime

############################### longtext ###############################
st_import = time.time()
timestamp_format = "%Y-%m-%d %H:%M:%S.%f"
ts_import = datetime.datetime.fromtimestamp(st_import).strftime(timestamp_format)
print(ts_import)

# Create an instance of PostgreSQLConnector
connector = MySQLConnector()

# Example query: SELECT schematic_id, features_vit FROM t_order_f;
table_name = connector.table
select_query = f"SELECT schematic_id, features_vit FROM {table_name}"

# Execute the query
results = connector.execute_query(select_query)

# Display the results
if results:
    print("Data import - success")


#timer for gettingdata - end
st_import_end = time.time()
ts_import_end = datetime.datetime.fromtimestamp(st_import_end).strftime(timestamp_format)
print(ts_import_end)
difference = st_import_end-st_import
print(f"Data import from DB(MySQL - longtext) completed in: {difference} sec")



############################### Array ###############################
#timer for getting data - start
st_import = time.time()
timestamp_format = "%Y-%m-%d %H:%M:%S.%f"
ts_import = datetime.datetime.fromtimestamp(st_import).strftime(timestamp_format)
print("\n",ts_import)

# Create an instance of PostgreSQLConnector
connector = PostgreSQLConnector()

# Example query: SELECT schematic_id, features_vit FROM t_order_f;
table_name = connector.table
select_query = sql.SQL("SELECT schematic_id, features_vit FROM {}").format(sql.Identifier(table_name))

# Execute the query
results = connector.execute_query(select_query)

# Display the results
if results:
    print("Data import - success")


#timer for gettingdata - end
st_import_end = time.time()
ts_import_end = datetime.datetime.fromtimestamp(st_import_end).strftime(timestamp_format)
print(ts_import_end)
difference = st_import_end-st_import
print(f"Data import from DB(numeric ARRAY) completed in: {difference} sec")


############################### JSON ###############################
#timer for getting data - start
st_import = time.time()
timestamp_format = "%Y-%m-%d %H:%M:%S.%f"
ts_import = datetime.datetime.fromtimestamp(st_import).strftime(timestamp_format)
print("\n",ts_import)

# Create an instance of PostgreSQLConnector
connector = PostgreSQLConnector()

# Example query: SELECT schematic_id, features_vit FROM t_order_f;
table_name = connector.table2
select_query = sql.SQL("SELECT schematic_id, features_vit_json FROM {}").format(sql.Identifier(table_name))

# Execute the query
results = connector.execute_query(select_query)

# Display the results
if results:
    print("Data import - success")


#timer for gettingdata - end
st_import_end = time.time()
ts_import_end = datetime.datetime.fromtimestamp(st_import_end).strftime(timestamp_format)
print(ts_import_end)
difference = st_import_end-st_import
print(f"Data import from DB(JSON) completed in: {difference} sec")


############################### JSONB ###############################
#timer for getting data - start
st_import = time.time()
timestamp_format = "%Y-%m-%d %H:%M:%S.%f"
ts_import = datetime.datetime.fromtimestamp(st_import).strftime(timestamp_format)
print("\n",ts_import)

# Create an instance of PostgreSQLConnector
connector = PostgreSQLConnector()

# Example query: SELECT schematic_id, features_vit FROM t_order_f;
table_name = connector.table3
select_query = sql.SQL("SELECT schematic_id, features_vit_jsonb FROM {}").format(sql.Identifier(table_name))

# Execute the query
results = connector.execute_query(select_query)

# Display the results
if results:
    print("Data import - success")


#timer for gettingdata - end
st_import_end = time.time()
ts_import_end = datetime.datetime.fromtimestamp(st_import_end).strftime(timestamp_format)
print(ts_import_end)
difference = st_import_end-st_import
print(f"Data import from DB(JSONB) completed in: {difference} sec")