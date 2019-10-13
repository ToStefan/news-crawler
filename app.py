from flask import Flask, jsonify
from flask_restful import Api

from resource import FcsCrawler, Hello

app = Flask(__name__)
api = Api(app)

api.add_resource(FcsCrawler, "/fcs-crawler")
api.add_resource(Hello, "/hello")

def app_main():
	app.run()

if __name__ == '__main__':
	app_main()