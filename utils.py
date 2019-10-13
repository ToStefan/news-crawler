import json
import os
import requests

from bs4 import BeautifulSoup

def file_to_json(filename):
	file = open(filename, encoding="utf-8")
	return json.load(file)

def get_request(url):
	return requests.get(url).text

def to_soup(data):
	return BeautifulSoup(data, 'html.parser')