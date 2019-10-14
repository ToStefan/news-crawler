from flask import Flask, jsonify
from flask_restful import Api

from resource import FcsCrawler, Hello

app = Flask(__name__)
api = Api(app)

api.add_resource(FcsCrawler, "/fcs-crawler")
api.add_resource(Hello, "/hello")

def app_main():
	app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
	app_main()