from bs4 import BeautifulSoup
import requests
import logging

class WebScraper:
    """WebScraper is a class for scraping data from a website."""

    def __init__(self, content, strategy, is_url=True):
        """Initialize the WebScraper with a URL or HTML content and a scraping strategy."""
        self.content = content
        self.is_url = is_url
        self.strategy = strategy

    def scrape(self):
        """Scrape the data from the website using the provided strategy."""
        if self.is_url:
            logging.info(f"Sending GET request to {self.content}")
            response = requests.get(self.content)
            logging.info("Parsing HTML content")
            soup = BeautifulSoup(response.text, 'html.parser')
        else:
            logging.info("Parsing HTML content")
            soup = BeautifulSoup(self.content, 'html.parser')

        self.strategy.soup = soup
        return self.strategy.scrape()
