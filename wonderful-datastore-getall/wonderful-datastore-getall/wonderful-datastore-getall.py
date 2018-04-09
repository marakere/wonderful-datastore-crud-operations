import sys
import logging
import rds_config
import pymysql

rds_host = db_host
name = db_name
password = db_password
db_name = db_name


def lambda_handler(event, context):
    """
    Establish the connection to Mysql Database
    Fetch the recent 20 rows from the table based on the timestamp
    """
    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""select itemkey, itemvalue from tabledatastore order by itemcreatetime DESC limit 20""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))

    return result
