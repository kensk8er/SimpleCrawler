# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class JobpostcrawlingItem(Item):
    # define the fields for your item here like:
    # name = Field()
    company_name = Field()
    job_name = Field()
    company_description = Field()
    job_description = Field()
    url = Field()
