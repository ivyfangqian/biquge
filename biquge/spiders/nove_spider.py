import scrapy
from biquge.items import BiqugeItem
from scrapy.http import Request

class NoveSpiderSpider(scrapy.Spider):
    name = 'nove_spider'
    allowed_domains = ['www.biqugeu.net']
    start_urls = ['https://www.biqugeu.net/64_64661/']

    def __init__(self):
        self.section_startpage_number = 0

    def parse(self, response):
        self.section_startpage_number = int(response.xpath("//dt[2]/following-sibling::dd[1]/a/@href").extract_first()[:-5].split('/')[-1])
        section_url_list = response.xpath("//dt[2]//following-sibling::dd//a/@href").extract()
        for i_section_url in section_url_list:
            yield Request("http://www.biqugeu.net" + i_section_url, callback=self.parse_section)

    def parse_section(self, response):
        biquge_item = BiqugeItem()
        biquge_item['novel_name'] = response.xpath("//div[@class='con_top']/a[2]/text()").extract_first()
        biquge_item['section_url'] = response.url
        biquge_item['section_number'] = int((biquge_item['section_url'])[:-5].split('/')[-1]) - self.section_startpage_number + 1
        biquge_item['section_name'] = response.xpath("//div[@class='bookname']/h1/text()").extract_first()
        biquge_item['section_content'] = response.xpath("//div[@id='content']/text()").extract()
        for i in range(len(biquge_item['section_content'])):
            biquge_item['section_content'][i] = biquge_item['section_content'][i].replace('\u3000\u3000', '\r\n')
        yield biquge_item

