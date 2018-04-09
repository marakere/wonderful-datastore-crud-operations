import sys
import logging
import rds_config
import pymysql


def lambda_handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into tabledatastore (itemkey, itemvalue, itemstatus) 
                values( '%s', '%s', '%s') ON DUPLICATE KEY UPDATE itemvalue='%s' ,itemstatus='%s'"""
                    % (event['itemkey'], event['itemvalue'], event['itemstatus'], event['itemvalue'],
                       event['itemstatus']))
    conn.commit()
    cur.close()


return "Added / Updated"
