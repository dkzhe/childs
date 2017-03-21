#!/usr/bin/python
#coding:utf-8

from DBUtils.PooledDB import PooledDB
import MySQLdb
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('rzc.conf')

class DB(object):
	def __init__(self):
		"""
		@return self.cursor
		"""
		#try:
		pool = PooledDB(MySQLdb,
			mincached = int(config.get('mysql','mincached')),
			maxcached = int(config.get('mysql','maxcached')),
			host = config.get('mysql','host'),
			user = config.get('mysql','user'),
			passwd = config.get('mysql','passwd'),
			db = config.get('mysql','db'))
		self.conn = pool.connection()
		self.cursor = self.conn.cursor()
	#	except Exception,e:
	#		print 'init'
	#		print e

	def get_exer(self,exerid):
		"""
		@get one exercise with exercise id
		"""
		if exerid.isdigit():
			try:
				sql = 'select exerid,content,b_answer from exercise where exerid = %d'
				param = (exerid,)
				self.cursor.execute(sql,param)
				result = self.cursor.fetchall()
			except Exception,e:
				print 'exer'
				print e
				result = e
		else:
			result = 'exerid is not a digit'
		return result

	def get_exers(self,n,*exerids):
		"""
		@get some exercises with exercises ids
		"""
		if isalldigit(exerids,n):
			try:
				sql = 'select exerid,content,b_answer from exercise where exerid in %s'
				p=', '.join(map(lambda x: '%s', exerids))
				sql = sql % p
				self.cursor.execute(sql,exerids)
				result = self.cursor.fetchall()
			except Exception,e:
				print 'exers'
				print e
				result = e
		else:
			result = 'exerids is not all digit'
		return result

	def get_answer(self,exerid):
		"""
		@get one answer with exercise id
		"""
		if exerid.isdigit():
			try:
				sql = 'select exerid,r_answer from exercise where exerid = %d'
				param = (exerid,)
				self.cursor.execute(sql,param)
				result = self.cursor.fetchall()
			except Exception,e:
				print 'answer'
				print e
				result = e
		else:
			result = 'exerid is not a digit'
		return result

	def get_answers(self,n,*exerids):
		"""
		@get some answers with exercise ids
		"""
		if isalldigit(exerids,n):
			try:
				sql = 'select exerid,r_answer from exercise where exerid in %s'
				p=', '.join(map(lambda x: '%s', exerids))
				sql = sql % p
				self.cursor.execute(sql,exerids)
				result = self.cursor.fetchall()
			except Exception,e:
				print 'answers'
				print e
				result = e
		else:
			result = 'exerids is not all digit'
		return result

	def set_score(self,userid,score):
		"""
		@update score with userid 
		"""
		if userid.isdigit() and score.isdigit():
			try:
				sql = 'update answer set score = %s where userid = %s'
				param = (userid,score)
				self.cursor.execute(sql,param)
				result = self.cursor.fetchall()
			except Exception,e:
				print 'score'
				print e
				result = e
		else:
			result = 'userid or score is not a digit'
		return result

	@staticmethod
	def isalldigit(n,*exerids):
		"""
		@ if the exerids list is all digit
		"""
		a = 1
		if len(exerids) == n:
			for e in exerids:
				print e
				print type(e)
				if str(e).isdigit():
					pass
				else:
					a = 0
					break
		else:
			a = 0
		return a

'''
if __name__ == '__main__':
	d = DB()
	print d.isalldigit(2,1,2)
'''
