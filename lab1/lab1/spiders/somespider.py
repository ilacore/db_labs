import scrapy

class SomeSpider(scrapy.Spider):
    name = "lab1"
    start_urls = ["http://uartlib.org/"]
    
    def parse(self, response):
        links = response.xpath("//img/@src")
        html = ""
        
        for link in links:
            url = link.get()
            
            if any(extension in url for extension in[".jpg",".png"]):
                html += """<a href="{url}" target="_blank">
                <img src="{url}" height=33% width=33%/>
                </a>""".format(url=url)

                with open("frontpage.html", "a") as page:
                    page.write(html)
                    page.close()
