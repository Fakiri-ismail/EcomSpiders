from random import randint
from src.core.utils import random_userAgent, split_between, to_csv_file, remove_file
from scrapy import Spider, Request
from src.items import ProductItem


class OunassSpider(Spider):
    name = "ounass"
    domain = "https://saudi.ounass.com"
    ua = random_userAgent()
    headers = {
        'referer': domain,
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': ua
    }

    cat_url = {
        "نساء": ["/women/shoes", "/women/bags", "/women/jewellery", "/women/beauty"],
        "رجال": ["/men/clothing", "/men/shoes", "/men/watches", "/men/bags", "/men/accessories"],
        "أطفال": ["/kids/girl", "/kids/boy", "/kids/baby", "/kids/shoes", "/kids/accessories"]
    }


    def start_requests(self):
        #remove_file()
        for category, urls in self.cat_url.items():
            for url in urls:
                yield Request(url=f"{self.domain}{url}", callback=self.parse_products, headers=self.headers, meta={"cat": category})

    def parse_products(self, response):
        products_url = response.css("li.StyleColorListItem > a::attr(href)")
        response.meta["sub_cat"] = response.css("nav.BreadcrumbNav span::text").getall()[-1]
        for product_url in products_url:
            url = f"{self.domain}{product_url.get()}"
            yield Request(url=url, callback=self.parse_product, headers=self.headers, meta=response.meta)

    def parse_product(self, response):
        item = ProductItem()
        item['_type'] = "simple"
        item['title'] = response.css("h1.PDPDesktop-name span::text").get()
        item['category'] = f"{response.meta['cat']} > {response.meta['sub_cat']}, {response.meta['cat']}"
        img_url_fix = "https://ounass-prod2.atgcdn.ae/pub/media/catalog/product/2/1/"
        imgs = response.css("div.ImageGallery-thumbnails picture link::attr(href)").getall()
        images = [f"{img_url_fix}{split_between(img, '/2/1/', '?')}" for img in imgs]
        item['image_url'] = ", ".join(images)
        product_price = response.css("div.PriceContainer span.PriceContainer-price::text").get()
        item['price'] = product_price.split(" ")[0]
        price = float(item['price'].replace(",","."))
        reduced_price = price - price * (randint(10,30) /100)
        item['reduced_price'] = str(reduced_price).replace(".", ",")
        item['stock'] = randint(20,100)
        item['available'] = 1
        item['short_description'] = response.css("main meta::attr(content)").get()
        description = ""
        for i in range(3):
            description_list = response.css(f"div#content-tab-panel-{i}.TabPanel p::text").getall()
            description += "\n".join(description_list) + "\n"
        item['description'] = description
        item['tax'] = "none"
        yield item
        #to_csv_file(item)
