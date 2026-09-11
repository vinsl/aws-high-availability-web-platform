import os

import pymysql


def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "support_desk"),
        password=os.getenv("DB_PASSWORD", "support_desk_password"),
        database=os.getenv("DB_NAME", "support_desk"),
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )