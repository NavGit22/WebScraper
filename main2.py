# IMDB Most Popular 100 Movies
from bs4 import BeautifulSoup
import requests
import pandas as pd

imdb_page = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

response = requests.get(imdb_page)
imdb_data = response.text
soup = BeautifulSoup(imdb_data, "html.parser")


all_movies = [movie for movie in soup.find_all('td', class_='titleColumn')]
all_ratings = [rating for rating in soup.find_all('td', class_='ratingColumn imdbRating')]

all_movie_names = []
all_movie_year = []
all_movie_cast = []
all_movie_title = []
all_movie_ratings = []

for movie in all_movies:
    for name in movie.findAll('a'):
        all_movie_names.append(name.text)
        all_movie_cast.append(name['title'])
        all_movie_title.append(name['href'])

    for year in movie.find('span'):
        if len(year.text) == 6:
            all_movie_year.append(year.text.replace('(', '').replace(')', ''))
        elif len(year.text) == 0:
            all_movie_year.append(' ')

for rating in all_ratings:
    try:
        all_movie_ratings.append(rating.find('strong')['title'])
    except TypeError:
        all_movie_ratings.append(" ")

outfile = {
    'movie name': all_movie_names,
    'movie year': all_movie_year,
    'movie cast & crew': all_movie_cast,
    'IMDB movie title': all_movie_title,
    'movie rating': all_movie_ratings
}
dataframe = pd.DataFrame(outfile)
dataframe.to_csv('top_100_movie_list.csv')
