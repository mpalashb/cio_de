# -*- coding: utf-8 -*-
import scrapy


class CioSpider(scrapy.Spider):
    name = 'cio'
    allowed_domains = ['cio.de']
    start_urls = ['https://www.cio.de/top500']

    def parse(self, response):

        elements = response.xpath('//*[@class="table idgTop500ListTable"]//tr')

        for res in elements:
            Rank     = res.xpath('.//*[@class="center"]//text()').extract_first().strip()
            Name     = res.xpath('.//td//a')
            if Name:
                Name = Name[0].xpath('.//text()').extract_first()
            Branche  = res.xpath('.//*[@class="idgBranchIconBigLink"]//@title').extract_first()


            if "Ranking" in Rank:
                print("<--------------------===---------------------->")
                print(f"Header {Rank}")
                print("<--------------------===---------------------->")

            else:
                yield {

                    'Rank':Rank,
                    'Name':Name,
                    'Branche':Branche


                }

        for link in range(2,21):
            next_page = f"https://www.cio.de/top500/nach-umsatz,1,{link}"
            yield scrapy.Request(next_page, callback=self.parse)
