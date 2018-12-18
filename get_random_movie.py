import codecs
from random import randint

filename = "watchlist.txt"

with codecs.open(filename,'r',encoding='utf8') as text_file:
	movies = text_file.readlines()

print(movies[randint(1, len(movies))])
input()