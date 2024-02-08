from urllib import request
import scrapy
from books.items import BooksItem

class SpiderbooksSpider(scrapy.Spider):
    name = "spiderbooks"
    allowed_domains = ["books.toscrape.com"]
    
    start_urls = []
    for i in range(1, 51):
        start_urls.append(f"https://books.toscrape.com/catalogue/page-{i}.html")

    def parse(self, response):
        
        for book in response.css("article.product_pod"):
            
            book_url = response.urljoin(book.css("h3 > a::attr(href)").extract_first())
            note = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}            

            yield scrapy.Request(book_url, callback=self.parse_book, meta={
                "titre": book.css("h3 > a::text").extract_first(),
                "price": book.css("p.price_color::text").extract_first(),
                "stock": [txt.strip() for txt in book.css("p.instock.availability::text").extract()][1],
                "rating": note[book.css("p.star-rating::attr(class)").extract_first().split(' ')[1]],
                #"url": book_url
            })

    def parse_book(self, response):
        yield BooksItem(
            titre=response.meta["titre"],
            price=response.meta["price"],
            stock=response.meta["stock"],
            category=response.css("ul.breadcrumb > li:nth-child(3) > a::text").extract_first(),
            rating=response.meta["rating"],
            description=' '.join(response.css("meta[name='description']::attr(content)").extract_first().split()).strip(),
            image_url=response.urljoin(response.css("img::attr(src)").extract_first())
            #url = response.meta["url"]
        )


