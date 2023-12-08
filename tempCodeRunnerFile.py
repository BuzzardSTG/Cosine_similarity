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