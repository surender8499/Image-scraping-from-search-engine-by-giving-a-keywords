from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import BaiduImageCrawler
from icrawler.builtin import FlickrImageCrawler

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,storage={'root_dir': 'your_image_dir'})
google_crawler.crawl(keyword='yadea brand logo', max_num=1000,min_size=(200,200), max_size=None)

bing_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4,storage={'root_dir': 'your_image_dir'})
bing_crawler.crawl(keyword='yadea brand logo', max_num=1000,min_size=(200,200), max_size=None)

baidu_crawler = BaiduImageCrawler(parser_threads=2, downloader_threads=4,storage={'root_dir': 'your_image_dir'})
baidu_crawler.crawl(keyword='yadea brand logo', max_num=1000,min_size=(200,200), max_size=None)

flickr_crawler = FlickrImageCrawler(parser_threads=2, downloader_threads=4,storage={'root_dir': 'your_image_dir'})
flickr_crawler.crawl(keyword='yadea brand logo', max_num=1000,min_size=(200,200), max_size=None)

