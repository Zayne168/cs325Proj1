import requests
from bs4 import BeautifulSoup
with open('urls.txt', 'r') as file:
    urls = file.readlines()
for idx, url in enumerate(urls):
    response = requests.get(url.strip())
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        content = soup.find('article').get_text()
    except AttributeError:
        print(f"Could not find article content in {url}")
        content = "No content available"

    with open(f'output_{idx}.txt', 'w') as output_file:
        output_file.write(content)