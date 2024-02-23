from bs4 import BeautifulSoup
import requests

resource = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2")
top_web = resource.text

soup = BeautifulSoup(top_web, "html.parser")
films = soup.find_all(name="h3", class_="title")
films_list= []
for film in films:
    film = film.text
    film = film.split(')')[-1]
    film = film.split("12:")[-1]
    films_list.insert(0,film)

count=1
with open("movies.txt", mode="w",encoding="utf-8") as file:
    for film in films_list:
        file.write(f"{count}) {film}\n")
        count +=1