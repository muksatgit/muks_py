import re
import logging

from webscraping.books.locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    A class to take in an HTML page or content, and find properties of an item in it.
    """
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New Book parser created from {parent}')
        self.parent = parent

    @property
    def name(self):
        logger.debug(f'Finding book Name')
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs['title']
        logger.info(f' Found book name, {item_name}')
        return item_name

    @property
    def link(self):
        logger.debug(f'Finding book Link')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.info(f' Found book link, {item_link}')
        return item_link

    @property
    def price(self):
        logger.debug(f'Finding book Price')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattren = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattren, item_price)
        price = float(matcher.group(1))
        logger.info(f' Found book price, {price}')
        return price

    @property
    def rating(self):
        logger.debug(f'Finding book rating')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)

        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.info(f' Found book rating, {rating_number}')
        return rating_number
