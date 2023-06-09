# This uses BeatifulSoup to scrape from a live website - https://news.ycombinator.com/news

import requests #Helps us to get hold of data from a particular url
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text    #Helps us to read the contents of the website in html code

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_texts = article_texts[::2]  #Other anchors cme in between
article_links = article_links[::2]
article_upvotes = [int(score.getText().split()[0]) for score in soup.select(selector=".score")]

# print(article_texts, article_links, article_upvotes, sep="\n")

max_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_index], article_links[max_index], article_upvotes[max_index], sep="\n")
