import pymysql
import traceback
from dbutils.pooled_db import PooledDB

pool = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=3,
    blocking=True,
    ping=0,
    db="py_redis",
    user="root",
    host="127.0.0.1",
    port=3306,
    passwd="xxxxxxxx",
    charset='utf8mb4'

)
conn = pool.connection()


def database_conn():
    try:
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return cursor
    except Exception:
        print(traceback.format_exc())


cursor = database_conn()
