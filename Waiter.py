import sqlite3 as sql
	
def Input(table, new):
	con = sql.connect('./DB.db')
	cur = con.cursor()

	query = 'SELECT "Orders" FROM "Queue" WHERE Tables='+str(table)
	cur.execute(query)
	prev = cur.fetchall()
	
	#query = 'SELECT "ID" FROM "Queue" WHERE "Tables"='+table
	#cur.execute(query)
	#ID = cur.fetchall()
	
	#query = 'SELECT * FROM '+ID[0][0]
	#cur.execute(query)
	#data = cur.fetchall()
	
	#print(ID[0][0])

	#for line in data:
	#	print("\x1b[0;0;44m" + line[0] +'     '+line[1]+'     '+line[2]+ '\x1b[0m')	
	
	
	#print("\nEnter order")
	
	#print("\x1b[0;0;42m"+'INPUT ORDER'+'\x1b[0m')
	order = prev[0][0] +' ' + str(new)
	#print(order)
	query = "UPDATE Queue SET Orders=\'"+order+"\' WHERE Tables="+str(table)
	cur.execute(query)
	
	con.commit()
	
	cur.close()
	con.close()

def Show(table):
	con = sql.connect('./DB.db')
	cur = con.cursor()
	
	query = 'SELECT "Orders" FROM "Queue" WHERE Tables='+str(table)
	cur.execute(query)
	prev = cur.fetchall()
	
	query = 'SELECT "ID" FROM "Queue" WHERE "Tables"='+str(table)
	cur.execute(query)
	ID = cur.fetchall()
	
	query = 'SELECT * FROM '+ID[0][0]
	cur.execute(query)
	data = cur.fetchall()
	
	#print(ID[0][0])
	out = str(ID[0][0]) + "\n" + "PREVIOUS ORDERS\n"
	
	for line in data:
		out = out + "\n"+ line[0] +'     '+line[1]+'     '+line[2]

	
	query = 'SELECT * FROM "Queue" WHERE Tables='+str(table)
	cur.execute(query)
	curent = cur.fetchall()
	#print("\n\nCURENT ORDER\n\nTable № "+ curent[0][1] + ' ' + curent[0][2])
	
	out = out + "\n\n\nCURENT ORDER\n\nTable № "+ curent[0][1] + ' ' + curent[0][2]

	cur.close()
	con.close()

	return(str(out))
	
		
def Read():
	con = sql.connect('./DB.db')
	cur = con.cursor()

	query_columns = 'pragma table_info(Queue)'
	cur.execute(query_columns)
	# Помещвем все полученные данные в переменную column_description
	columns_description = cur.fetchall() 
	# Помещаем название колонок в соответствующую переменную
	columns_names = []
	
	for column in columns_description:
		columns_names.append(column[0])
	
	query = 'SELECT "Tables" FROM "Queue"'
	cur.execute(query)
	data = cur.fetchall()
	# Сейчас data это список кортежей - это не удобно, переделаем его в список
	new_data = []
	for element in data:
		new_data.append(element[0])
	data = new_data
	del(new_data)
	# Выведем data не как список а как строчки	
	
	out = "\nWAITING TABLES:\n"
	#print("\nWAITING TABLES:\n")
	for line in data:
		#print("\x1b[0;0;44m" +'Table № ' + line + '\x1b[0m')
		out = out + "\nTable № " + line	
	#print (str(out))
	
	cur.close()
	con.close()

	return(str(out))
		
def Close(table):
	con = sql.connect('./DB.db')
	cur = con.cursor()

	query = 'SELECT "Orders" FROM "Queue" WHERE Tables='+str(table)
	cur.execute(query)
	order = cur.fetchall()
	
	query = 'SELECT "ID" FROM "Queue" WHERE "Tables"='+str(table)
	cur.execute(query)
	ID = cur.fetchall()
	
	query = "UPDATE "+ID[0][0]+" SET Orders=\'"+order[0][0]+"\' WHERE Orders = 'Empty'"
	cur.execute(query)
	
	query = "DELETE FROM Queue WHERE Tables="+str(table)+""
	cur.execute(query)
	
	con.commit()
	
	cur.close()
	con.close()

	
if __name__ == '__main__':	
	con = sql.connect('./DB.db')
	cur = con.cursor()
	
	while True:
		Read()
		print ("\nTo Update:		enter u\n\nTo Serve:		enter s\n\nTo stop:		enter stop\n")
		comand = str(input("> "))
	
		if comand == 'u':
			print("\x1b[0;0;42m"+'UPDATE'+'\x1b[0m')
			Read()
	
		elif comand == 's':
			print("Enter table number")
			table = str(input("> "))
				
			print ("\nTo Input:		 enter i\n\nTo close		enter c\n")
			comand = str(input("> "))
			
			if comand == 'i' :
				Input(table)
			elif comand == 'c' :
				print("\x1b[0;0;42m"+'CLOSE'+'\x1b[0m')
				Close(table)
			else:
				print('\x1b[0;0;41m' + "TRY AGAIN" + '\x1b[0m')
				
		
		elif comand == 'stop':
			break
	
		else:
			print('\x1b[0;0;41m' + "TRY AGAIN" + '\x1b[0m')
	cur.close()
	con.close()
	
