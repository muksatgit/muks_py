from bs4 import BeautifulSoup

from webscraping.scraping_quotes.locators.quote_page_locators import QuotesPageLocators
from webscraping.scraping_quotes.parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')


    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.soup.select(QuotesPageLocators.QUOTE)]