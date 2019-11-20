import scrapy

class textspider(scrapy.Spider) :
    name = "text"


    def start_requests(self):
        urls = [
            "https://academicintegrity.org/day-against-contract-cheating"
            #"https://www.frontiersin.org/articles/10.3389/feduc.2018.00067/full"
        ]
        #allowed_domains = ['urls']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        #link = response.xpath('//a/@href').extract()
        #tag = response.xpath('//a/text()').extract()
        all = response.xpath('//p/text()').extract()
        #url = self.urls
        #all= all.replace('\xa0',' ')

        #for a in all:
            #text = a.xpath('text()').extract()
        all = str(all)
        yield{
        #    'url' : url
            'text' : all
            }
