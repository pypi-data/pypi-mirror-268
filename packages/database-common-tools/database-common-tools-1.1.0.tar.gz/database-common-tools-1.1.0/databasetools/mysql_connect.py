import pymysql

def mysql_connect(host, user, password, database):
    pymysql.connect(host=host,user=user,password=password,database=database)

def find_by_query(connect, query):
    find_cursor = connect.cursor()
    find_cursor.execute(query)
    return find_cursor.fetchall()