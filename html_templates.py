from utils import write_file

fcs_pages_path = "data/html/"

def fcs_each_column(slika, naslov, link):
	return \
		"            <div class=col-2 style=margin:10px> " + \
		"                <a href=" + link + " style=width:100% >" + \
		"                    <img src=" + slika + " style=width:100% >" + \
		"                </a>" + \
		"                <h6 style=text-align:center;width:100%; >" + \
		"                    " + naslov + \
		"                </h6>" + \
		"            </div>"

def fcs_news_template(columns):
	return \
		'<!DOCTYPE html>' + \
		'<html>' + \
		'<head>' + \
		'    <title>FCS NEWS</title>' + \
		'<link rel=stylesheet href=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css integrity=sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T crossorigin=anonymous>' + \
		'<script src=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js integrity=sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM crossorigin=anonymous></script>' + \
		'</head>' + \
		'<body>' + \
		'    <div class=container>' + \
		'        <h1>FILMSKI CENTAR SRBIJE - NOVOSTI' + \
		'        <div class=row>' + \
		columns + \
		'        </div>' + \
		'    </div>' + \
		'</body>' + \
		'</html>'

def render_fcs_news(json_list):
	columns = ""
	for index, each in enumerate(json_list):
		link = render_fcs_page(each["content"], index)
		columns += fcs_each_column(each["slika"], each["naslov"], link)
	return fcs_news_template(columns)

def fcs_page_template(content):
	return \
		'<!DOCTYPE html>' + \
		'<html>' + \
		'<head>' + \
		'    <title>Page example</title>' + \
		'<link rel=stylesheet href=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css integrity=sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T crossorigin=anonymous>' + \
		'<script src=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js integrity=sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM crossorigin=anonymous></script>' + \
		'</head>' + \
		'<body>' + \
		'    <div class=container-fluid>' + \
		content + \
		'    </div>' + \
		'</body>' + \
		'</html>'

def render_fcs_page(content, id):
	name = 'pages/fcs_example_page_' + str(id) + '.html'
	content = fcs_page_template(content)
	#write_file(fcs_pages_path + name, content)
	write_file(fcs_pages_path + name, content.replace('\"', ''))
	return name