import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import pymongo

# Environment variable
load_dotenv()
MONGO_CONN = os.getenv('MONGO_CONN')
print(MONGO_CONN)

# Scrape function
def scrape_quotes():
    more_links = True
    page = 1
    quotes = []
    while(more_links):
        markup = requests.get(f'http://quotes.toscrape.com/page/{page}').text
        soup = BeautifulSoup(markup, 'html.parser')
        for item in soup.select('.quote'):
            quote = {}
            quote['text'] = item.select_one('.text').get_text()
            quote['author'] = item.select_one('.author').get_text()
            tags = item.select_one('.tags')
            quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
            quotes.append(quote)

        next_link = soup.select_one('.next > a')

        # print which page was scraped
        print("scraped page:",page)

        # check if the next link element exists
        if(next_link):
            page += 1
        else:
            more_links = False
    return quotes

quotes = scrape_quotes()

# print all scraped quotes
print(quotes)

# Storing in MongoDB

client = pymongo.MongoClient(MONGO_CONN)
db = client.db.quotes
try:
    db.insert_many(quotes)
    print(f"inserted {len(quotes)} articles")
except:
    print("an error occurred quotes were not stored to db")


