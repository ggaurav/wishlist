import cherrypy
import json, traceback, os
from dbcon import DBCon 

def handleException(status):
	traceback.print_exc()
	cherrypy.response.status = status
	return json.dumps({'msg': traceback.format_exc()})

#Ideally REST api urls should have been like 
#/getAllItems
#/<user_id>/getWishlist
#/<user_id>/addToWishlist
#/<user_id>/deleteFromWishlist

#properly handle error cases, for e.g. in case of unautorized user return 401
class CherryController:
	def index(self, **params):		
		return open(os.path.join(".", 'index.html'))
	index.exposed=True

	#user_id hardcoded for now
	def getAllItems(self, **params):
		try:
			db = DBCon()
			qry = "select id, title, img from items"			
			data = db.fetch_all(qry)
			qry = "select item_id from wishlist"
			wishListItems = db.fetch_all(qry)			
			ids = [elem['item_id'] for elem in wishListItems]														
			return json.dumps({'data':data, 'wishlistItemIds': ids})
		except :
			return handleException(500)
	getAllItems.exposed = True

	def getWishlist(self, **params):
		try:
			db = DBCon()
			qry = "select item_id from wishlist where user_id = 1"			
			data = db.fetch_all(qry)
			ids = [elem['item_id'] for elem in data]				
			return json.dumps({'data': {'ids': ids}})
		except:
			return handleException(500)
	getWishlist.exposed = True

	def addToWishlist(self, **params):
		try:
			db = DBCon()
			item_id = int(params['item_id'])
			qry = "insert into wishlist values (null, %d, 1)" %(item_id)
			db_resp = db.insert(qry)
			if not db_resp:
				raise ('Unable to add item to wishlist')
			return json.dumps({'data': {}})
		except:
			return handleException(500)
	addToWishlist.exposed = True

	def deleteFromWishlist(self, **params):
		try:
			db = DBCon()
			item_id = int(params['item_id'])
			qry = "delete from wishlist where user_id = 1 and item_id =  %d" %(item_id)
			db_resp = db.delete(qry)			
			if not db_resp:
				raise ('Unable to delete item from wishlist')
			return json.dumps({'data': {}})
		except:
			return handleException(500)
	deleteFromWishlist.exposed = True

if __name__ == '__main__':
	cherrypy.config.update({'server.socket_host': '127.0.0.1','server.socket_port': 1008})
	cherrypy.quickstart(CherryController() , "/")	