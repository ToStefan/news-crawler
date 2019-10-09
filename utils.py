import json
import os
import requests

from bs4 import BeautifulSoup

def write_file(file_name, data):
	with open(file_name, "w+", encoding="utf-8") as f:
		f.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

def clear():
	if(os.name =="nt"):
		os.system("cls")
	else:
		os.system("clear")

def file_to_json(filename):
	file = open(filename, encoding="utf-8")
	return json.load(file)

def get_request(url):
	return requests.get(url).text

def to_soup(data):
	return BeautifulSoup(data, 'html.parser')