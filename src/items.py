# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ProductItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field(deprecated='Product Name')
    image_url = Field(deprecated='Product Image')
    sponsored = Field(deprecated='Is Sponsored')
    price = Field(deprecated='Price')
    rating_count = Field(deprecated='Rating Count')
    rating_value = Field(deprecated='Rating Value')
