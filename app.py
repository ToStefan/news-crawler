from flask import Flask
from flask_restful import Api

from resource import FcsCrawler, Hello

APP = Flask(__name__)
API = Api(APP)

API.add_resource(FcsCrawler, "/fcs-crawler")
API.add_resource(Hello, "/hello")

def app_main():
	APP.run(host='0.0.0.0')

if __name__ == '__main__':

	app_main()
