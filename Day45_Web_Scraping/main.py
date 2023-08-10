from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

contents = requests.get(URL).text
soup = BeautifulSoup(contents, "lxml")

# articles = soup.find_all(name="a", class_="titlelink")
# article_texts = []
# article_links = []
# article_upvotes = [int(upvote.getText().split(' ')[0]) for upvote in soup.find_all(name="span", class_="score")]
# for article in articles:
#     article_texts.append(article.getText())
#     article_links.append(article.get("href"))
# print(article_texts)
# print(article_links)
# print(article_upvotes)
# highest_upvote = max(article_upvotes)
# index = article_upvotes.index(highest_upvote)
# highest_text = article_texts[index]
# highest_link = article_links[index]
# print(highest_text)
# print(highest_link)
titles = soup.find_all(name="h3", class_="title")
titles_text = [title.getText() for title in titles][::-1]
print(titles)
# with open("movies.txt", "w", encoding="utf-8") as f:
#     for title in titles_text:
#         f.write(title + "\n")
