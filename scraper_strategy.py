from abc import ABC, abstractmethod


class ScraperStrategy(ABC):
    """Base class for different website scraping strategies."""

    def __init__(self, soup):
        """Initialize the strategy with a BeautifulSoup object."""
        self.soup = soup

    @abstractmethod
    def scrape(self):
        """Scrape the data from the website."""
        pass
