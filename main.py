import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL, verify=False)
films_web_page = response.text

soup = BeautifulSoup(films_web_page, "html.parser")
title_tags = soup.find_all(name="h3", class_="title")
title_texts = [tag.getText() for tag in title_tags]
title_texts.reverse()

with open("films.txt", "w", encoding="utf-8") as file:
    for text in title_texts:
        file.write(f"{text}\n")

