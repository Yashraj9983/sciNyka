import scrapy
# from ..items import sku
import json
class NykSpider(scrapy.Spider):
    name = "nyk"
    allowed_domains = ["nykaa.com"]
    start_urls = ["https://www.nykaa.com/brands/lakme/c/604?page_no=1&sort=popularity&eq=desktop"]    
    urls_list=[]
    def parse(self, response):        
        self.urls_list+= response.css('a.css-qlopj4::attr("href")').getall()
        url1=response.url        
        url2=url1.replace("page_no=1","page_no=2")
        yield scrapy.Request(url2,callback=self.parse2)
        
    def parse2(self, response):                    
        self.urls_list+= response.css('a.css-qlopj4::attr("href")').getall()
        for i in range(24):
            url="https://www.nykaa.com"+self.urls_list[i]
            yield scrapy.Request(url,callback=self.parse_prod)


    def parse_prod(self,response):        
        json_data=response.css("script::text").getall()[3]
        data=json.loads(json_data[29:])
        size=data["dataLayer"]["product"]["packSize"]
        prod=data["productPage"]["product"]
        name=prod["name"]
        price=prod["offerPrice"]
        availability='Out of Stock'
        if prod["inStock"] :
                availability="Available"
        variantList=[]
        for variants in prod["variants"]:
            name2=variants["name"]
            price2=variants["offerPrice"]            
            availability2='Out of Stock'
            if variants["inStock"] :
                availability2="Available"
            packsize=variants["packSize"]    
            variantList.append({"name":name2,
                            "price":price2,
                            "availability":availability2,
                            "pack_size":packsize})
        yield {"name":name,
                "price":price,
                "availability":availability,
                "pack_size":size,
                "variants":variantList}
        
        

        # skuids=response.css(".css-51qmmz button::attr('id')").getall()
        # if len(skuids)>1:
        #     skuids=[i[8:] for i in skuids]
        #     for i in skuids:
        #         url2=response.url+"&skuId="+i
        #         yield scrapy.Request(url2,callback=self.parse_sku)

        # else:
        #     yield {'url':response.url,
        #        'name':response.css(".css-1gc4x7i::text").get(),
        #        'colors':response.css(".css-2t5nwu option::text").getall()[5:],
        #        'count':len(response.css(".css-2t5nwu option::text").getall()[5:]),               
        #        'price':response.css("div.css-1d0jf8e span.css-1jczs19::text").get()
        #        }
    # def parse_sku(self,response2):
        
    #     avail=response2.css(".css-38zjd7 span::text").get()
    #     if len(avail)<3:
    #         avail="Available"

    #     yield {'url':response2.url,               
    #     'name':response2.css(".css-1gc4x7i::text").get(),
    #     'avail':avail,
    #     'price':response2.css("div.css-1d0jf8e span.css-1jczs19::text").get()
    #     }
        # sku1=sku()    
        # sku1['url']=response.url
        # sku1['name']=response.css(".css-1gc4x7i::text").get()
        # sku1['avail']=response.css(".css-38zjd7 span::text").get()
        # sku1['price']=response.css("div.css-1d0jf8e span.css-1jczs19::text").get()

        # return sku1


