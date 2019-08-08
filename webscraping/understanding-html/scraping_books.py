import  requests
import bs4


page = requests.get("http://books.toscrape.com")
print(page.content)
