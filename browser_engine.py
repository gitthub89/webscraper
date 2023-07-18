from selenium import webdriver
import logging

class BrowserEngine:
    """BrowserEngine is a class for handling browser operations using Selenium."""

    def __init__(self, driver_path):
        """Initialize the BrowserEngine with a path to the webdriver executable."""
        self.driver_path = driver_path
        self.browser = None

    def start_browser(self):
        """Start a new browser instance."""
        logging.info("Starting browser")
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()

    def get_page(self, url):
        """Navigate to a URL."""
        logging.info(f"Navigating to {url}")
        self.browser.get(url)

    def get_page_source(self):
        """Get the HTML source of the current page."""
        logging.info("Fetching page source")
        return self.browser.page_source

    def close_browser(self):
        """Close the browser instance."""
        logging.info("Closing browser")
        self.browser.quit()
