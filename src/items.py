# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ProductItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = Field(deprecated='Product ID')
    _type = Field(deprecated='Product Type')
    title = Field(deprecated='Product Name')
    category = Field(deprecated='Category')
    image_url = Field(deprecated='Product Image')
    sponsored = Field(deprecated='Is Sponsored')
    price = Field(deprecated='Price')
    reduced_price = Field(deprecated='Reduced Price')
    stock = Field(deprecated='Stock')
    available = Field(deprecated='Is Available')
    short_description = Field(deprecated='Short Description')
    description = Field(deprecated='Description')
    tax = Field(deprecated='Tax')
    rating_count = Field(deprecated='Rating Count')
    rating_value = Field(deprecated='Rating Value')
    