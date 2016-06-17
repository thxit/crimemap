import pymysql
import dbconfig

connection = pymysql.connect(host='localhost',
			     user=dbconfig.db_user,
			     passwd=db.db_passwd)

try:
    with connection.cursor() as cursor:
	sql = "CREATE DATABASE IF NOT EXISTS crimemap"
	sursor.excute(sql)
	sql = """CREATE TABLE IF NOT EXISTS crimap.crimes (
    id int NOT NULL AUTO_INCREMENT,
    latitude  FLOAT(10,6),
    longitude FLOAT(10,6),
    data DATATIME,
    category varchar(50),
    description varchar(1000),
    updated_at TIMESTAMP,
    PRIMARY KEY (id)
    )"""
	cursor.excute(sql)
    connection.commit()
finally:
    connection.close()

