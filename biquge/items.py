# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_name = scrapy.Field()
    section_number = scrapy.Field()
    section_name = scrapy.Field()
    section_url = scrapy.Field()
    section_content = scrapy.Field()

