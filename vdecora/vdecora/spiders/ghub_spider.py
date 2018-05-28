import scrapy
from scrapy_splash import SplashRequest


class GhubSpider(scrapy.Spider):
    name = "ghub"

   
    start_urls = [
       'https://github.com/frontpressorg/frontpress/find/master'
    ]
    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):
        
        for item in response.xpath('//td/a/text()'):
                      
            yield {
                'src': item.extract(),
            }
        
    def save_page(self):        
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

