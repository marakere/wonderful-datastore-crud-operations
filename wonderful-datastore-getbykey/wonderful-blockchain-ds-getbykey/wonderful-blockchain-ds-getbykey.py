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
    - Connect to Mysql database
    - Fetch the row from a table based on the key passed by client
    """

    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""select itemkey, itemvalue from tabledatastore where itemkey = '%s'""" % (event['itemkey']))
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))

    return result
