
from utils import clear, get_request, to_soup, write_file
from fcs_render import fcs_render_main

news_json_path = "data/news.json"

def content_crawler(link):
	request = get_request(link)
	soup = to_soup(request)
	main_content = soup.find("div", {"id": "inner-block"})
	main_content = str(main_content.find("img", {"class", "attachment-medium-feature size-medium-feature wp-post-image"}))
	main_content = main_content.replace('\n', '<br />')
	return main_content

def news_crawler(soup):
	news = soup.find_all("div", {"class": "vest_container"})
	news_len = str(len(news))
	news_json_list = []

	for index, each in enumerate(news):

		print("Procesuira: " + str(index + 1) + "/" + news_len)

		datum = each.find("div", {"class", "meta"}).text
		slika = each.find("img")["src"]
		opis = each.find("p").text
		naslov = each.find("h2").text
		tip = each.find("div", {"class", "img_desc"}).text
		link = each.find("a")["href"]
		content = content_crawler(link)

		news_json_list.append({
			"naslov": naslov,
			"datum": datum, 
			"slika": slika,
			"opis": opis,
			"tip": tip,
			"link": link,
			"content": content})

	return news_json_list
	
def crawler_main():
	request = get_request("http://www.fcs.rs/category/vesti/")
	soup = to_soup(request)
	news_json_list = news_crawler(soup)
	write_file(news_json_path, news_json_list)

if __name__ == '__main__':
	clear()
	crawler_main()
	fcs_render_main()