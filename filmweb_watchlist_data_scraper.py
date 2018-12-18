### login, haslo, range podawany z palca !!! ###
import requests
from requests_html import HTMLSession
import codecs

payload = {'j_username': 'apap549',
	'j_password': '**********'}
mojaLista = []
filename = "watchlist_new.txt"

with codecs.open(filename,'w',encoding='utf8') as text_file:
	with HTMLSession() as s:
		p = s.post('https://www.filmweb.pl/j_login', data=payload)
		r = s.get('https://www.filmweb.pl/j_login')
		for x in range(1,19):
			path = 'https://www.filmweb.pl/user/apap549/wantToSee?page='+str(x)
			print(path)
			r = s.get(path)

			film = r.html.find('.filmPreview__title')
			rok = r.html.find('.filmPreview__year')

			licznik = 0
			for title in film:
				mojaLista.append(title.text)
				print(title.text)
				text_file.write(title.text +" "+rok[licznik].text+ '\n')
				licznik=licznik +1