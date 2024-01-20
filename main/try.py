import requests
from bs4 import BeautifulSoup
import urllib.parse


def scan(url):
    wordlist_file = "small.txt"

    with open(wordlist_file, "r") as file:
        for line in file:
            directory = line.strip("\n")
            main_url = url + "/" + directory
            response = requests.get(main_url)
            if response.status_code == 200:
                print(" statuse code 200 >> " + main_url)
            elif response.status_code != 200 and response.status_code != 400:
                print(" status code " + str(response.status_code) + " >> " + main_url)


starting_url = 'https://example.com'
scan(starting_url)