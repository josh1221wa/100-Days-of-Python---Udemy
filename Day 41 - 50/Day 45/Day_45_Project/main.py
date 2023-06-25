# Scrape the best 100 movies from https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/ and put it in a txt file from 1 to 100

import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
page = response.text

soup = BeautifulSoup(page, "html.parser")

titles = [title.getText()+"\n" for title in soup.select(selector="h3", class_="title")]
titles.reverse()

with open("movies.txt", "w+", encoding="utf-8") as f:
    f.writelines(titles)

