from pyquery import PyQuery as pq


class BookmarksTodb():
	def __init__(self, filename='utils/bookmarks_2020_5_5_win.html'):
		with open(filename, 'r+', encoding='utf-8') as file:
			self.html = file.read()
			self.doc = pq(self.html)

	def get_cage_list(self):
		cage_li = []
		items = self.doc('H3')
		for cage in items:
			cage_li.append(cage.text)
		return cage_li

	def get_url_list(self):
		lis = self.doc('A').items()
		datas = []
		for li in lis:
			url_params = {}
			url_params['url'] = li.attr('href')
			url_params['title'] = li.text()
			print(url_params)
			datas.append(url_params)
		return datas




