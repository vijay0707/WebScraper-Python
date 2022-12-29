# WebScraper-Python
![webscraping-python](https://github.com/vijay0707/WebScraper-Python/blob/master/web-scraping-with-python.png)
Quotes web scraper using Python-BeautifulSoup Library and MongoDB

### website to be scraped : [http://quotes.toscrape.com/](http://quotes.toscrape.com/)
Quotes.toscrape was built to practice web scraping.

### Prerequsites:
- python 3

### Creating the project
Create a folder on your machine, then open your terminal and cd into that folder. Now we’ll need to create a virtual environment so on your terminal run:

**``python3 -m venv env``**

Wait for it’s completion and you’ll see that an env folder was created inside your folder. This will contain the packages we’ll install later, that Python will need to run your project.

Let’s activate the virtual environment:
**Note: In windows, run the commands in git bash. For command prompt, commands will be slightly different kindly google it 🙂**

#### for linux/macOs:
**``source env/bin/activate``** 

#### for windows:
**``source env/scripts/activate``** 

### Installing the dependencies
Run the following command:
**``pip install -r requirements.txt``** 

### Creating a cluster in mongodb
#### Refer: [mongo-db-cluster-setup](https://www.mongodb.com/basics/clusters/mongodb-cluster-setup)
