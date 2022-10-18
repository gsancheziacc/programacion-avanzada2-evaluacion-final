import mysql.connector


def get_connection():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='Admin1234+', db='PAIIEF')
    return conn


def close_connection(conn):
    conn.close()
