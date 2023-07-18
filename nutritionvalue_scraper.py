from scraper_strategy import ScraperStrategy
import logging

class NutritionValueScraper(ScraperStrategy):
    """Scraping strategy for nutritionvalue.org."""

    def scrape(self):
        """Scrape the data from the website."""
        logging.info("Scraping data from nutritionvalue.org")

        table = self.soup.find('table', class_='center wide cellpadding3 nutrient results')
        nutrients = []
        amounts = []

        # Skip the first two rows (headers)
        for row in table.find_all('tr')[2:]:
            cells = row.find_all('td')
            if len(cells) >= 2:
                nutrient = cells[0].get_text(strip=True)
                amount = cells[1].get_text(strip=True)
                nutrients.append(nutrient)
                amounts.append(amount)

        return dict(zip(nutrients, amounts))
