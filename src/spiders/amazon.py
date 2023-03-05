from src.items import ProductItem
from scrapy import Spider, Request


class AmazonSpider(Spider):
    name = "amazon"
    domain = "https://www.amazon.com"
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
    headers = {
        'referer': domain,
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': ua
    }

    cat_url = "/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A502394&ref=nav_em__nav_desktop_sa_intl_camera_and_photo_0_2_5_3"

    def start_requests(self):
        url = f"{self.domain}{self.cat_url}"
        yield Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        products = response.css(".s-widget-spacing-small .sg-col-inner")
        #remove_file()
        for product in products:
            item = ProductItem()
            item['title'] = product.css(".a-size-base-plus::text").get()
            item['image_url'] = product.css(".s-image::attr(src)").get()
            item['sponsored'] = True if product.css(".s-sponsored-label-info-icon").get() else False
            item['price'] = product.css(".a-price span::text").get()[1:]
            rating_value = product.css("i.a-icon-star-small > span::text").get().split(" ")[0]
            rating_count = product.css("span.a-size-base.s-underline-text::text").get()[1:-1].replace(",", "")
            item['rating_value'] = float(rating_value) if rating_value else None
            item['rating_count'] = int(rating_count) if rating_count else 0
            #to_csv_file(item)
            yield item
