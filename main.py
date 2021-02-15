import requests
from bs4 import BeautifulSoup

URl = "https://www.esquire.com/entertainment/movies/g226/best-movies-ever-0609/"

response = requests.get(URl)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
#print(soup)
all_movies = soup.find_all(class_="listicle-slide-hed-text")
#print(all_movies)
movies_titles = [movie.getText() for movie in all_movies]

#print(movies_titles[::-1])
movies = movies_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")