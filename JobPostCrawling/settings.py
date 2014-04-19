# Scrapy settings for JobPostCrawling project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'JobPostCrawling'

SPIDER_MODULES = ['JobPostCrawling.spiders']
NEWSPIDER_MODULE = 'JobPostCrawling.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'JobPostCrawling (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 1
#ROBOTSTXT_OBEY = True
