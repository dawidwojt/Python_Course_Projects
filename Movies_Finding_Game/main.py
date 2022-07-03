from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
archieve_web_page = response.text
soup = BeautifulSoup(archieve_web_page, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")

movies_list = []

for movie_title in movie_titles:
    title = movie_title.getText()
    movies_list.append(title)


movies_list.reverse()

with open("movies_list.txt", mode="w") as file:
    for i in movies_list:
        file.write(f"{str(i)}\n")

print(movies_list)