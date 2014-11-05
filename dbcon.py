import MySQLdb as mdb
import sys, traceback
import time
from threading import Lock

#Sould have used connection pooling
class DBCon(object):
	host = 'localhost'
	db = 'wishlist'
	user = 'root'
	passwd = ''
	_instance = None
	lock = Lock()

	def __new__(cls):
		if not cls._instance:
			cls.lock.acquire()
			if not cls._instance:
				cls._instance = super(DBCon, cls).__new__(cls)
				#cls._instance.init()
			cls.lock.release()
		return cls._instance

	def insert(self, query):
		con = None
		res = None
		try:
			con = mdb.connect(self.host, self.user, self.passwd, self.db)
			#cursor = con.cursor(mdb.cursors.DictCursor)
			cursor = con.cursor()
			cursor.execute(query)
			res = cursor.lastrowid
			con.commit()
			
		except:
			traceback.print_exc()
		finally:
			if con:
				con.close()
		return res

	def update(self, query):
		con = None
		try:
			con = mdb.connect(self.host, self.user, self.passwd, self.db)
			cursor = con.cursor()
			cursor.execute(query)
			con.commit()
			return True
		except:
			traceback.print_exc()
			return False
		finally:
			if con:
				con.close()	


	def delete(self, query):
		return self.update(query)

	def fetch_one(self, query):
		con = None
		res = None
		try:
			con = mdb.connect(self.host, self.user, self.passwd, self.db)
			cursor = con.cursor(mdb.cursors.DictCursor)
			cursor.execute(query)
			res = cursor.fetchone()
		except:
			traceback.print_exc()
		finally:
			if con:
				con.close()
		return res



	def fetch_all(self, query):
		con = None
		res = []
		try:
			con = mdb.connect(self.host, self.user, self.passwd, self.db)
			cursor = con.cursor(mdb.cursors.DictCursor)
			cursor.execute(query)
			res = cursor.fetchall()
		except:
			traceback.print_exc()
		finally:
			if con:
				con.close()
		return res

