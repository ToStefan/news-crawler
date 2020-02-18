import json
import csv
import codecs

import requests
from bs4 import BeautifulSoup
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

SOFTWARE_NAMES = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value]
OPERATING_SYSTEMS = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
USER_AGENT_ROTATOR = UserAgent(software_names=SOFTWARE_NAMES,
								operating_systems=OPERATING_SYSTEMS,
								limit=100)

def to_soup(data):
	return BeautifulSoup(data, 'lxml')

def get_request(url):
	user_agent = USER_AGENT_ROTATOR.get_random_user_agent()
	headers = {"User-Agent": user_agent}

	response = requests.get(url, headers=headers)
	return response.text

def dict_to_json(file_name, data):
	with open(file_name, "w+", encoding="utf-8") as file:
		file.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

def json_to_dict(filename):
	with open(filename, 'rb') as file:
		return json.load(file)

def dict_to_csv(csv_name, dict_list):
	keys = dict_list[0].keys()
	output_file = codecs.open(csv_name, "w", encoding="utf-16")
	dict_writer = csv.DictWriter(output_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(dict_list)
	output_file.close()
	