import requests
from bs4 import BeautifulSoup                               #import scrapper
with open('urls.txt', 'r') as file:                         #take in file with list of URLS
    urls=file.readlines()                                   #goes line by line reading the file(reading the urls)
for idx, url in enumerate(urls):                            #for #of lines in url(.txt), loop through the number of lines used (enumerate would say "5")
    response=requests.get(url.strip())                      
    soup=BeautifulSoup(response.content, 'html.parser')     #Beautiful soup does its thang

    with open(f'output_{idx}.txt', 'w') as output_file:     #write to output files like a G
        output_file.write(soup.get_text())