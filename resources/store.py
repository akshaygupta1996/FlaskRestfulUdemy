from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

	def get(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json()
		return {"message": "Store Not Found"}, 404

	def post(self, name):
		if StoreModel.find_by_name(name):
			return {"message": "Store '{}' Already Exists".format(name)}, 400

		store = StoreModel(name)
		try:
			store.save_to_db()
		except:
			return {'message': 'Error Occured'}, 500
		return store.json(),200


	def delete(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db(name)

		return {'message': 'Store Deleted'}


class StoreList(Resource):
	
	def get(self):
		return {'stores': [store.json() for store in StoreModel.query.all()]}

		