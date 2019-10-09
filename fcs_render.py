

from html_templates import render_fcs_news
from utils import file_to_json, write_file, clear


news_json_path = "data/news.json"
fcs_news_example_html = "data/html/fcs_news_example.html"

def fcs_render_main():
	fcs_json_list = file_to_json(news_json_path)
	html = render_fcs_news(fcs_json_list)
	write_file(fcs_news_example_html, html)

if __name__ == '__main__':
	clear()
	fcs_render_main()