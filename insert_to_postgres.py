import os
import connection
import sqlparse
import pandas as pd
from datetime import datetime


if __name__ == '__main__':
    print('[INFO] Service ETL is Starting ...')

    # connection dwh
    conf_dwh = connection.config('dwh')
    conn_dwh, engine_dwh = connection.psql_conn(conf_dwh, 'DataWarehouse')
    cursor_dwh = conn_dwh.cursor()

    # Drop table if it exists
    drop_table_query = "DROP TABLE IF EXISTS total_orders_based_on_month_rendragi;"
    cursor_dwh.execute(drop_table_query)
    conn_dwh.commit()

    # Create data mart table in Postgres 
    create_table_query = '''
    CREATE TABLE total_orders_based_on_month_rendragi (
        month VARCHAR(7),
        total_orders INTEGER
    );
    '''

    try:
        # Execute create table query
        cursor_dwh.execute(create_table_query)
        conn_dwh.commit()
        print('[INFO] Successfully created table total_orders_based_on_month_rendragi')

        # Read data from file
        with open(os.getcwd()+'/output/Wordercount_output_hadoop_map.txt', 'r') as file:
            lines = file.readlines()

        # Convert data to appropriate format
        data = []
        for line in lines:
            parts = line.strip().split("\t")  
            date = parts[0].strip('"')
            total_orders = int(parts[1])
            data.append((date, total_orders))

        # Insert data into table
        insert_query = "INSERT INTO total_orders_based_on_month_rendragi (month, total_orders) VALUES (%s, %s);"
        cursor_dwh.executemany(insert_query, data)

        conn_dwh.commit()
        print('[INFO] Successfully imported data to table total_orders_based_on_month_rendragi')

        print('[INFO] Service ETL is Success ...')
    except Exception as e:
        print(e)
        print('[INFO] Service ETL is Failed ...')
