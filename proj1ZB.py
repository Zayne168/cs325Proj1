import requests
from bs4 import BeautifulSoup
with open('urls.txt', 'r') as file:                                                     #opens urls.txt file included in folder (as variable "file")
    urls = file.readlines()                                                             #reads each individual line into a seperate piece of an array
for idx, url in enumerate(urls):                                                        #indexes through the urls array
    response = requests.get(url.strip())                                                #beautiful soup scraps the url of the index
    soup = BeautifulSoup(response.content, 'html.parser')                               #beautiful soup scraps the url of the index

    try:                                                                                #checks if the url has title and description data available first
        title = soup.find('title').get_text()                                           
        synopsis = soup.find('meta', attrs={'name': 'description'})['content']          #if there is data on the article then it will save it in the title and synopsis("description") variables
    except (AttributeError, KeyError):                                                  #if there isnt a data in the article it will spit an error to tell you.
        print(f"Could not find title or synopsis in {url}")
        title = "No title available"
        synopsis = "No synopsis available"

    with open(f'output_{idx}.txt', 'w') as output_file:                                 
        output_file.write(f"Title: {title}\nSynopsis: {synopsis}")                      #index through the number of outputs to be made and writes to the file.
