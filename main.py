import logging
from webscraper import WebScraper
from nutritionvalue_scraper import NutritionValueScraper
from browser_engine import BrowserEngine
from csvwriter import CSVWriter

# Set up logging
logging.basicConfig(level=logging.INFO)

# Start a new browser instance
browser = BrowserEngine('/path/to/geckodriver')
browser.start_browser()

# Use the classes to scrape a website and output the data to a CSV file
browser.get_page("https://www.nutritionvalue.org/Pasta%2C_enriched%2C_dry_nutritional_value.html")
page_source = browser.get_page_source()
scraper = WebScraper(page_source, NutritionValueScraper(None), is_url=False)
nutrition_data = scraper.scrape()

# Transform the data into a list of tuples and write it to a CSV file
nutrition_data_list = [(nutrient, amount) for nutrient, amount in nutrition_data.items()]
writer = CSVWriter('nutrition_data.csv')
writer.write(nutrition_data_list, headers=['Nutrient', 'Amount'])

# Close the browser when you're done
browser.close_browser()
