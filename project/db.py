import mysql.connector


class Database():

	def connect(cls):
		try:
			conn=mysql.connector.connect(user='root',password='test',host='localhost',database='site_1')
			return conn
		except mysql.connector.Error as err:
			print(err)

	def delete_from(cls,table,col=None,val=None):

		conn=cls.connect()
		cursor=conn.cursor()
		if col!=None and val!=None:
			pass
		else:
			try:
				query=f'DELETE FROM {table}'
				cursor.execute(query)
				conn.commit()
				print(f'{cursor.rowcount} in {table} deleted')
			except mysql.connector.Error as err:
				print(err)
			finally:
				cursor.close()
				conn.close()

	def insert_into(cls,table,*args):
		conn=cls.connect()
		cursor=conn.cursor()
		val=(args)
		try:
			if table=='rate':
				query=f'INSERT INTO {table} (d_rate,d_xrate,p_rate,p_xrate,y_rate,y_xrate,e_rate,e_xrate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
				cursor.execute(query,val)
				conn.commit()
				print(f'{cursor.rowcount} in {table} updated')

			if table=='wiki_search':
				query=f'INSERT INTO {table} (title,user,content,img,url) VALUES (%s,%s,%s,%s,%s)'
				cursor.execute(query,val)
				conn.commit()
				print(f'{cursor.rowcount} in {table} updated')
			
			if table=='twitter_timeline':
				query=f'INSERT INTO {table} (created,text,link,name,img) VALUES (%s,%s,%s,%s,%s)'
				cursor.execute(query,val)
				conn.commit()
				print(f'{cursor.rowcount} in {table} updated')

			if table=='imdb_movie':
				query=f'INSERT INTO {table} (title,year,runtime,genre,director,actors,plot,poster,rating,production) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
				cursor.execute(query,val)
				conn.commit()
				print(f'{cursor.rowcount} in {table} updated')

			if table=='yt_channels':
				query=f'INSERT INTO {table} (user,title,views,href) VALUES (%s,%s,%s,%s)'
				cursor.execute(query,val)
				conn.commit()
				print(f'{cursor.rowcount} in {table} updated')

			if table=='science_news':
				query=f'INSERT INTO {table} (source,img,link,title,text,meta) VALUES (%s,%s,%s,%s,%s,%s)'
				cursor.execute(query,val)
				conn.commit()
				print(f'{cursor.rowcount} in {table} updated')

			if table=='events':
				query=f'INSERT INTO {table} (username,event,hour,descreption,type_e,date) VALUES (%s,%s,%s,%s,%s,%s)'
				cursor.execute(query,val)
				conn.commit()
				print(f'{cursor.rowcount} in {table} updated')

			if table=='popluer_machine':
				query=f'INSERT INTO {table} (link,img,title,content,author) VALUES (%s,%s,%s,%s,%s)'
				cursor.execute(query,val)
				conn.commit()
				print(f'{cursor.rowcount} in {table} updated')

		except mysql.connector.Error as err:
			print(err)
		finally:
			cursor.close()
			conn.close()

	def select_from(cls,table,col=None,val=None):
		conn=cls.connect()
		cursor=conn.cursor()

		if col!=None and val!=None:
			query=f'SELECT * FROM {table} WHERE {col}="{val}"'
			cursor.execute(query)
			data=cursor.fetchall()
			return data
		else:
			try:
				query=f'SELECT * FROM {table}'
				cursor.execute(query)
				data=cursor.fetchall()
				return data
			except mysql.connector.Error as err:
				print(err)
			finally:
				cursor.close()
				conn.close()
			

		