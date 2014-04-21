from collections import defaultdict
import os
from re import match
import sys

__author__ = 'kensk8er'

from datetime import datetime

from scrapy.contrib.spiders import SitemapSpider
from scrapy.selector import Selector

from JobPostCrawling.items import JobpostcrawlingItem


class JobPostCrawler(SitemapSpider):
    name = 'job_post_crawler'
    allowed_domains = ['targetjobs.co.uk']
    sitemap_urls = [
        'http://targetjobs.co.uk/sites/targetjobs.co.uk/files/sitemap.xml',
    ]
    sitemap_rules = [
        # regular expression + method name
        (r'/employer-hubs/.*/.*', 'parse_content'),
    ]

    def parse_content(self, response):
        sel = Selector(response)
        item = JobpostcrawlingItem()
        item['company_name'] = sel.xpath('//div[@class="ad-content-header"]/h1/text()').extract()[0]

        if match(r'.*organisation-profile', response.url):
            # procedures for company pages
            target = sel.css('.hreview-aggregate > p')
            target.extend(sel.css('.hreview-aggregate > ul > li'))
            item['company_description'] = '\n'.join(''.join(p.xpath('.//text()').extract()) for p in target)
            item['url'] = response.url
            yield item
        else:
            # procedures for job post pages
            try:
                save_content = sel.xpath('//div[@id="save-content"]/a/text()').extract()[0]
                organisation_link = sel.xpath('//p[@class="organisation-link"]/a/text()').extract()[0]
                item['job_name'] = sel.xpath('//div[@class="main-content-core"]/h2/text()').extract()[0]
                target = sel.css('.hreview-aggregate > p')
                target.extend(sel.css('.hreview-aggregate > ul > li'))
                item['job_description'] = '\n'.join(''.join(p.xpath('.//text()').extract()) for p in target)
                item['url'] = response.url
                yield item
            except:
                pass


# for debug
if __name__ == '__main__':
    args = sys.argv
    if len(args) == 5:
        file_name = args[4]
        os.system('rm ' + file_name)
        from scrapy.cmdline import execute

        execute()
        pass
    else:
        print 'invalid arguments (4 arguments required)'
