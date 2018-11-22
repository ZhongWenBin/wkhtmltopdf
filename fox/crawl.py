from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import time
import logging
import os
from scrapy.utils.project import get_project_settings


configure_logging()

runner = CrawlerRunner(get_project_settings())

@defer.inlineCallbacks
def crawl():
    logging.info("new cycle starting")
    yield runner.crawl('read')
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished
os.system("python readpipeline.py")
