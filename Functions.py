import time
import sqlite3 as sql

def Create(ID):
	con = sql.connect('./DB.db')
	cur = con.cursor()
	
	query = "CREATE TABLE IF NOT EXISTS "+ID+" ('Date' TEXT, 'Tables' TEXT, 'Orders' TEXT)"
	cur.execute(query)
	con.commit()
	
	query = "CREATE TABLE IF NOT EXISTS Queue ('ID' TEXT, 'Tables' TEXT, 'Orders' TEXT)"
	cur.execute(query)
	
	cur.close()
	con.close()

def Write(ID, table):
	con = sql.connect('./DB.db')
	cur = con.cursor()
	
	date = time.strftime("%Y.%m.%d %H:%M:%S")
	#order = str(input("> "))
	order = "Empty"
	empty = 'Order: '
	unit = [date, table, order]
	
	query = "INSERT INTO "+ID+" VALUES(?, ?, ?)"
	cur.execute(query, unit)
	
	unit = [ID, table, empty]	
	query = "INSERT INTO Queue VALUES(?, ?, ?)"
	cur.execute(query, unit)
	
	con.commit()
	
	cur.close()
	con.close()
	
def Output(ID):
	con = sql.connect('./DB.db')
	cur = con.cursor()
	
	query_colomns = 'pragma table_info('+ID+')'
	cur.execute(query_colomns)
	columns_description = cur.fetchall()
	
	columns_names = []
	for column in columns_description:
		columns_names.append(column[0])
		
	query = 'SELECT * FROM '+ID
	cur.execute(query)
	data = cur.fetchall()
	
	for line in data:
		print(line)
	
	cur.close()
	con.close()
