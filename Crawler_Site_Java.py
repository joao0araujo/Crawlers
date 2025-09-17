import csv
import json
import requests
from bs4 import BeautifulSoup

lista_de_posts = []

url = "https://www.guiadojava.com.br/search"

response = requests.get(
    url,
    params={"q": "jsp"}
)

# print(response.content)

contexto = BeautifulSoup(response.content, 'html.parser')

seleciona_posts = contexto.select(".blog-posts.hfeed.container .post-outer")

print(seleciona_posts[0].select(".post-title.entry-title")[0].text.strip())