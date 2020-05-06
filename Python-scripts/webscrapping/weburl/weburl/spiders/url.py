import scrapy

class textspider(scrapy.Spider) :
    name = "link"


    def start_requests(self):
        urls = [
            "https://academicintegrity.org/day-against-contract-cheating"
        #    "https://www.frontiersin.org/articles/10.3389/feduc.2018.00067/full"
        ]
        #allowed_domains = ['urls']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        #link = response.xpath('//a/@href').extract()
        #tag = response.xpath('//a/text()').extract()
        all = response.xpath('//a')

        for a in all:
            link = a.xpath('@href').extract()
            tag = a.xpath('text()').extract()

            #if (link == '.*')
            #    link = link.replace(',',url)


            yield{
                'urls' : link,
                'tags' : tag
                }
