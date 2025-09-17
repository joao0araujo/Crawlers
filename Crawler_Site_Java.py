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

print(response.content)