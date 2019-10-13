from utils import get_request, to_soup

def content_scraper(link):
	request = get_request(link)
	soup = to_soup(request)
	main_content = soup.find("div", {"id": "inner-block"})
	main_content = str(main_content.find("img", {"class", "attachment-medium-feature size-medium-feature wp-post-image"}))
	main_content = main_content.replace('\n', '<br />')
	return main_content

def news_crawler(soup):
	news = soup.find_all("div", {"class": "vest_container"})
	news_json_list = []

	for each in news:

		datum = each.find("div", {"class", "meta"}).text
		slika = each.find("img")["src"]
		opis = each.find("p").text
		naslov = each.find("h2").text
		tip = each.find("div", {"class", "img_desc"}).text
		link = each.find("a")["href"]
		content = content_scraper(link)

		news_json_list.append({
			"naslov": naslov,
			"datum": datum, 
			"slika": slika,
			"opis": opis,
			"tip": tip,
			"link": link,
			"content": content})

	return news_json_list
	
def fcs_crawler_main():
	request = get_request("http://www.fcs.rs/category/vesti/")
	soup = to_soup(request)
	news_json_list = news_crawler(soup)
	return news_json_list