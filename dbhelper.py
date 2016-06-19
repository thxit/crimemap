#coding=utf-8
import pymysql
import dbconfig


class DBHelper:
    
  def connect(self, database="crimemap"):
    return pymysql.connect(host='localhost',
    	  port=3406, # this is very imporant if you changed sql port. I waste losts of time
	      user=dbconfig.db_user,
	      passwd=dbconfig.db_password,
	      db=database)
            
  def get_all_inputs(self):
    connection = self.connect()
    query = "SELECT description FROM crimes;"
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
    return cursor.fetchall()
      

  def add_input(self,data):
    connection = self.connect()
    try:
	    #The following introduces a deliberate security flaw
	    #Mitigating sql injection by using %s placeholder
      query = "INSERT INTO crimes (description) VALUES (%s);"
      with connection.cursor() as cursor:
        cursor.execute(query,data)
        connection.commit()#这里tab和空格混用将导致错误：IndentationError: unexpected indent

    finally:
      connection.close()


  def clear_all(self):
    connection = self.connect()
    try:
      query = "DELETE FROM crimes;"
      with connection.cursor() as cursor:
	      cursor.execute(query)
	      connection.commit()
    finally:
      connection.close()

			
