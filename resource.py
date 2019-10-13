from flask import jsonify
from flask_restful import Resource

from fcs_crawler import fcs_crawler_main

class FcsCrawler(Resource):
	def get(self):
		news_json_list = fcs_crawler_main()
		return jsonify(news_json_list)

class Hello(Resource):
	def get(self):
		return jsonify({"message": "Hello!"})