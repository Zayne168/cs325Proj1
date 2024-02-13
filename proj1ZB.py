import requests
from bs4 import BeautifulSoup
with open('urls.txt', 'r') as file:
    urls = file.readlines()
for idx, url in enumerate(urls):
    response = requests.get(url.strip())
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        title = soup.find('title').get_text()
        synopsis = soup.find('meta', attrs={'name': 'description'})['content']
    except (AttributeError, KeyError):
        print(f"Could not find title or synopsis in {url}")
        title = "No title available"
        synopsis = "No synopsis available"

    with open(f'output_{idx}.txt', 'w') as output_file:
        output_file.write(f"Title: {title}\nSynopsis: {synopsis}")

