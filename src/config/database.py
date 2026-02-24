import os
import psycopg2
from psycopg2.extras import RealDictCursor


def get_db_connection():
    return psycopg2.connect(
        host="aws-1-us-east-1.pooler.supabase.com",
        port=5432,
        database="postgres",
        user="postgres.xmhyrqqinocuxsiyplfe",
        password="A74082124%axel",
        cursor_factory=RealDictCursor,
    )


def get_one(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return result


def get_all(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def execute(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()


def get_last_insert_id(table, id_column="id"):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT LASTVAL() as {id_column}")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[id_column] if result else None
