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

# print(seleciona_posts[0].select(".post-title.entry-title")[0].text.strip())

for post in seleciona_posts:
    titulo = post.select(".post-title.entry-title a")[0].text.strip()
    link = post.select(".snippet-fade.r-snippet-fade")[0].get("href")
    conteudo = post.select(".snippet-item.r-snippetized")[0].text.strip()

    dados = {
        "titulo": titulo,
        "link": link,
        "conteudo": conteudo,
    }

    lista_de_posts.append(dados)

for i in lista_de_posts:
    print(i["titulo"])