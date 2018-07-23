1.import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='maainul',
                             #db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new database
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (id int NOT NULL AUTO_INCREMENT,latitude FLOAT(10,6),longitude FLOAT(10,6),date DATETIME,category VARCHAR(50),description VARCHAR(1000),updated_at TIMESTAMP,PRIMARY KEY (id))"""
        cursor.execute(sql,)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
