import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from tabulate import tabulate
from halo import Halo
import lxml

MAIN_URL = "https://www.python.org"

ua = UserAgent()

headers = {"user-agent": ua.random}

spinner = Halo(text='Loading', spinner='dots')
spinner.start()

response = requests.get(MAIN_URL, headers=headers)

spinner.stop()


soup = BeautifulSoup(response.text, features="lxml")

events_block = soup.find(class_="medium-widget event-widget last")
events_menu = events_block.find_all("li")

parse_events_list = []

for i in events_menu:
    _, event_data, event_name = i.text.split("\n")
    event_link = MAIN_URL + i.find("a")["href"]
    parse_events_list.append([event_data, event_name, event_link])

print(tabulate(parse_events_list, headers=["Date", "Name", "Link"], tablefmt="github"))
