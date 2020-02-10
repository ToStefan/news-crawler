from utils import get_request, to_soup

FCS_URL = "http://www.fcs.rs/category/vesti/"
ATTRS_TO_REMOVE = ["srcset", "alt", "id", "class", "height", "width", "sizes", "style"]

def remove_attributes(soup):
	for div in soup.find_all("div"): div.decompose()
	for script in soup.find_all("script"): script.decompose()

	for attribute in ATTRS_TO_REMOVE:
		for tag in soup.find_all(attrs={attribute: True}):
			del tag[attribute]
	return soup

def clear_content(soup):
	return str(soup) \
				.replace('\n', '<br />') \
				.replace("<div class=\"min_700\" id=\"inner-block\">", "") \
				.replace("</div>", "")

def scrap_content(url):
	res = get_request(url)
	soup = to_soup(res)

	content = soup.find("div", {"id": "inner-block"})
	content = remove_attributes(content)
	return clear_content(content)

def crawl_articles(url):
	res = get_request(url)
	soup = to_soup(res)
	divs = soup.find_all("div", {"class": "vest_container"})
	news_data = []

	for div in divs:
		date = div.find("div", {"class", "meta"}).text
		picture = div.find("img")["src"]
		description = div.find("p").text
		title = div.find("h2").text
		tip = div.find("div", {"class", "img_desc"}).text
		url = div.find("a")["href"]
		content = scrap_content(url)
		news_data.append({
			"title": title,
			"date": date, 
			"picture": picture,
			"description": description,
			"type": tip,
			"url": url,
			"content": content})
	return news_data
	
def fcs_crawler():
	return crawl_articles(FCS_URL)

if __name__ == '__main__':
	from utils import dict_to_json
	data = fcs_crawler()
	dict_to_json("JSON_IGNORE.json", data)