from fcs_crawler import fcs_crawler

from flask import jsonify
from flask_restful import Resource

class FcsCrawler(Resource):
	def get(self):
		data = fcs_crawler()
		return jsonify(data)

class Hello(Resource):
	def get(self):
		return jsonify({"message": "Hello!"})