import scrapy
from ..items import ImdbItem  # Import the class from items.py.

class ImdbSpider(scrapy.Spider):
    name = 'imdb'  # Define a variable for the project.
    # Define the main web address to extract info.
    start_urls = ["https://www.imdb.com/list/ls004610270/?st_dt=&mode=detail&page=1&sort=list_order,asc&ref_=ttls_vm_dtl"]

    def parse(self, response):

        # Define and compile the links to get the details of needed info.
        hrefs = response.css("div.lister-item-content a ::attr(href)").extract()
        for href in hrefs:
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_page)

        # Define the link of next page to get info from multiple pages.
        next_page = response.css("a.flat-button.lister-page-next.next-page ::attr(href)")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    def parse_page(self, response):

        item = ImdbItem()  # Create the item object with reference to class in items.py

        # Define variables for each feature, use scrapy.css selector to get the necessary info and
        # use properties and methods such as indexing, slicing, split and strip.
        film_name = response.css('div.title_wrapper h1::text').extract()[0].strip()
        film_date = response.css('div.subtext a::text').getall()[-1]).strip().split('(')[0]
        film_country = response.css('div.subtext a::text').getall()[-1].strip(')\n').split('(')[-1]
        film_rate = response.css('div.ratingValue span::text').extract()[0]
        director = response.css('div.credit_summary_item a::text').extract()[0]
        stars = response.css('div.credit_summary_item a::text').extract()[-4:-1]

        # Create pairs of keys, values for each item in our dictionary and aggregate them with yield.
        item['Film_Name'] = film_name
        item['Film_Date'] = film_date
        item['Film_Country'] = film_country
        item['Film_Rate'] = film_rate
        item['Director'] = director
        item['Stars'] = stars
        yield item
