from flask_restful import Resource, reqparse
# import sqlite3
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
				type = float,
				required = True,
				help = "this field cannot be left blank"
			)
	parser.add_argument('store_id',
				type = int,
				required = True,
				help = "Store Id is necessary"
			)
	@jwt_required()
	def get(self, name):
		# for item in items:
		# 	if item['name'] == name:
		# 		return {'item': item}, 200
		# # item = next(filter(lambda x: x['name'] == name, items), None)
		# return {'item': None}, 404
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()

		return {'message': 'Item Not Found'}, 404



	def post(self, name):
		# if next(filter(lambda x: x['name'] == name, items), None):

		# for item in items:
		# 	if item['name'] == name:
		# 		return {'message': "An item with name '{}' already exists".format(name)},400
		# data = request.get_json(silent=True)
		
		if ItemModel.find_by_name(name):
			return {'message': "An Item with name '{}' already exists.".format(name)}, 400

		data = Item.parser.parse_args()
		item = ItemModel(name, data['price'], data['store_id'])
		# item = {'name': name, 'price': data['price']}
		# items.append(item)
		try:
			# ItemModel.insert(item)
			item.save_to_db()
		except:
			return {"message": "An error occured"}, 500
		
		return item.json(), 201


	
	def delete(self, name):
		# global items
		# items = list(filter(lambda x: x['name']!=name, items))
		
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# query = "DELETE FROM items WHERE name=?"
		# cursor.execute(query, (name,))

		# connection.commit()
		# connection.close()

		item = ItemModel.find_by_name(name)
		if item:
			item.delete_from_db()


		return {'message': 'Item Deleted'}

	def put(self, name):
		
		# data = request.get_json()
		data = Item.parser.parse_args()

		# item_found = None
		# for item in items:
		# 	if item['name'] == name:
		# 		item_found = item
		# # item = next(filter(lambda x: x['name']==name, items), None)
		

		# if item_found is None:
		# 	item_found = { 'name': name, 'price': data['price']}
		# 	items.append(item_found)
		# else:
		# 	item_found.update(data)
		# return item_found

		item = ItemModel.find_by_name(name)
		# updated_item = {'name':name,'price': data['price']}
		# updated_item = ItemModel(name, data['price'])
		if item is None:
			item = ItemModel(name, data['price'], data['store_id'])
			# try:
			# 	# ItemModel.insert(updated_item)
			# 	updated_item.insert()
			# except:
			# 	return {"message": "An Error Occured inserting the new item"}, 500

		else:
			item.price = data['price']
		item.save_to_db()
			# try:
			# 	# ItemModel.update(updated_item)
			# 	updated_item.update()
			# except:
			# 	return {"message": "An Error occured updating the new item"}, 500
		# return updated_item.json()
		return item.json()

	

class ItemList(Resource):
	def get(self):

		return {'items': [item.json() for item in ItemModel.query.all()]}

		# connection  = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# query = "SELECT * FROM items"
		# result = cursor.execute(query)
		# items = []
		# for row in result:
		# 	items.append({'name': row[0], 'price': row[1]})

		# connection.commit()
		# # connection.close()
		# return {'items': items}
