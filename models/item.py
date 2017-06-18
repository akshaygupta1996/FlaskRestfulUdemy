import sqlite3
from db import db


class ItemModel(db.Model):

	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))
	store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
	store = db.relationship('StoreModel')

	def __init__(self, name,price, store_id):
		self.name = name;
		self.price  =price
		self.store_id = store_id

	def json(self):
		return {'id': self.id, 'name': self.name, 'price': self.price}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name = name).first()

		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# query = "SELECT * FROM items WHERE name=?"
		# result = cursor.execute(query, (name,))
		# row = result.fetchone()
		# connection.close()

		# if row is not None:
		# 	# return {'item': {'name': row[0], 'price': row[1]}}
		# 	return cls(*row)
	# @classmethod
	# def insert(cls, item):
	# def insert(self):
	def save_to_db(self):
		# this function can now both insert and save to database
		db.session.add(self)
		db.session.commit()


		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# query = "INSERT INTO items VALUES(?,?)"
		# cursor.execute(query, (self.name, self.price))

		# connection.commit()
		# connection.close()

	# @classmethod
	# def update(cls, item):
	# def update(self):
	# 	connection  = sqlite3.connect('data.db')
	# 	cursor = connection.cursor()

	# 	query = "UPDATE items SET price=? WHERE name = ?"
	# 	cursor.execute(query, (item['price'], item['name']))

	# 	connection.commit()
	# 	connection.close()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
