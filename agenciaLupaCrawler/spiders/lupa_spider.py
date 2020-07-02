import scrapy
from ..items import AgencialupacrawlerItem
#Esta spider e responsavel por coletar as informacoes das noticias na pagina
#inical da lupa

class LupaSpider(scrapy.Spider):
    name = "lupa"
    page_number = 2

    def start_requests(self):
        urls = [
            'https://piaui.folha.uol.com.br/lupa/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = AgencialupacrawlerItem()
        blocos = response.css(".bloco .inner")
        for bloco in blocos:
            title = bloco.css(".bloco-title a::text").extract()[0]
            author = bloco.css(".bloco-autor::text").extract()[0]
            date = bloco.css(".bloco-meta::text").extract()[0]
            time = bloco.css(".bloco-meta .time::text").extract()[0]
            abstract = bloco.css(".bloco-chamada a::text").extract()[0]
            link = bloco.css(".bloco-chamada a::attr(href)").get()
        
            items['title'] = title
            items['author'] = author
            items['date'] = date
            items['time'] = time
            items['abstract'] = abstract
            items['link'] = link

            yield items

        # ir para proxima pagina
        next_page = 'https://piaui.folha.uol.com.br/lupa/page'+str(LupaSpider.page_number)+'/'   
        if LupaSpider.page_number < 5:
            LupaSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)