from fcs_crawler import fcs_crawler

from flask import jsonify
from flask_restful import Resource

class FcsCrawler(Resource):
	@staticmethod
	def get():
		data = fcs_crawler()
		return jsonify(data)

class Hello(Resource):
	@staticmethod
	def get():
		return jsonify({"message": "Hello!"})
		