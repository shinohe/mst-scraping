# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import os
import re

currentDir = os.path.dirname(os.path.abspath(__file__))
flaskPath = currentDir + os.sep 
filePath = flaskPath + 'data' + os.sep 

class MstGamerchSpider(scrapy.Spider):
    name = "mst_gamerch_spider"
    allowed_domains = ['xn--cckza4aydug8bd3l.gamerch.com']
    # FIXME 後で外部プロパティ化
    search_words = [
#            '/★1',
#            '/★2',
#            '/★3',
#            '/★4',
            '/★5']
    pageNum = 0
    count = 0

    def start_requests(self):
        urls = [
            'https://xn--cckza4aydug8bd3l.gamerch.com',
        ]
        for word in self.search_words:
            for url in urls:
                url = url + word
                yield scrapy.Request(url=url, callback=self.search)

    def search(self, response):
        pageNum = 0
        for table in response.css('section.ui_article_content.ui_article_auth.ui_article_entry table').extract():
            for href in response.css('tbody td.no-min-width:first-child a::attr(href)').extract():
                self.log('href: %s' % href)
                url = 'https://xn--cckza4aydug8bd3l.gamerch.com' + href
                self.log('url: %s' % url)
#                yield scrapy.Request(url, callback=self.parse)
                return scrapy.Request(url, callback=self.parse)
                
#        for href in response.css('#content_2_2 ~ table > tbody a::attr(href)').extract():
#            self.log('href: %s' % href)
#            url = response.url + href
#            yield scrapy.Request(url=url, callback=self.parse)
#
#        for href in response.css('#content_2_3 ~ table > tbody a::attr(href)').extract():
#            self.log('href: %s' % href)
#            url = response.url + href
#            yield scrapy.Request(url=url, callback=self.parse)
#
#        for href in response.css('#content_2_4 ~ table > tbody a::attr(href)').extract():
#            self.log('href: %s' % href)
#            url = response.url + href
#            yield scrapy.Request(url=url, callback=self.parse)
#
#        for href in response.css('#content_2_5 ~ table > tbody a::attr(href)').extract():
#            self.log('href: %s' % href)
#            url = response.url + href
#            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log('parse: %s' % response.url)
        self.log(response.css('div.ui_wikidb_top_pc p a::text').extract())
        self.log(response.css('div.ui_wikidb_top_pc p::text').extract())
        self.log(response.css('div.ui_wikidb_top_pc ~ p::text').extract())
        self.log(response.css('div.ui_wikidb_middle_pc p::text').extract())
        self.log(response.css('div.ui_wikidb_middle_area.ui_clearfix > p::text').extract())
        
        name = response.css('h2#js_wikidb_main_name::text').extract()[0]
        
        shusshin = response.css('div.ui_wikidb_top_pc p a::text').extract()[0]
        
        nenrei = response.css('div.ui_wikidb_top_pc p::text').extract()[2]
        seibetsu = response.css('div.ui_wikidb_top_pc p::text').extract()[4]
        
        rarelity = response.css('div.ui_wikidb_top_pc p a::text').extract()[1]
        
        zokusei = response.css('div.ui_wikidb_top_pc p::text').extract()[8]
        
        seichouType = response.css('div.ui_wikidb_top_pc ~ p::text').extract()[0]
        buki = response.css('div.ui_wikidb_top_pc ~ p::text').extract()[2]
        bukiShubetsu = response.css('div.ui_wikidb_top_pc ~ p a::text').extract()[0]
        doujiKougekisuu = response.css('div.ui_wikidb_top_pc ~ p::text').extract()[6]
        kougekiDansuu = response.css('div.ui_wikidb_top_pc ~ p::text').extract()[8]
        if len(kougekiDansuu) == 1:
            kougekiDansuu = '1'
        else:
            kougekiDansuu = kougekiDansuu[1:-1]
        print(kougekiDansuu)
        
        shokiHp = response.css('div.ui_wikidb_middle_pc p::text').extract()[0]
        saidaiHp = response.css('div.ui_wikidb_middle_pc p::text').extract()[1]
        kakuseiHp = response.css('div.ui_wikidb_middle_pc p::text').extract()[2]
        idousokudo = response.css('div.ui_wikidb_middle_pc p::text').extract()[3]
        reach = response.css('div.ui_wikidb_middle_pc p::text').extract()[4]
        dps = response.css('div.ui_wikidb_middle_pc p::text').extract()[5]
        kakuseiDps = response.css('div.ui_wikidb_middle_pc p::text').extract()[6]
        
        shokiKougeki = response.css('div.ui_wikidb_middle_area.ui_clearfix > p::text').extract()[0]
        saidaiKougeki = response.css('div.ui_wikidb_middle_area.ui_clearfix > p::text').extract()[1]
        kakuseiKougeki = response.css('div.ui_wikidb_middle_area.ui_clearfix > p::text').extract()[2]
        kougekiKankaku = response.css('div.ui_wikidb_middle_area.ui_clearfix > p::text').extract()[3]
        toughness = response.css('div.ui_wikidb_middle_area.ui_clearfix > p::text').extract()[4]
        sougouDps = response.css('div.ui_wikidb_middle_area.ui_clearfix > p::text').extract()[5]
        kakuseiSougouDps = response.css('div.ui_wikidb_middle_area.ui_clearfix > p::text').extract()[6]
        
        name = name.replace(',','')
        shusshin = shusshin.replace(',','')
        nenrei = nenrei.replace(',','')
        seibetsu = seibetsu.replace(',','')
        rarelity = rarelity.replace(',','')
        zokusei = zokusei.replace(',','')
        seichouType = seichouType.replace(',','')
        buki = buki.replace(',','')
        bukiShubetsu = bukiShubetsu.replace(',','')
        doujiKougekisuu = doujiKougekisuu.replace(',','')
        kougekiDansuu = kougekiDansuu.replace(',','')
        shokiHp = shokiHp.replace(',','')
        saidaiHp = saidaiHp.replace(',','')
        kakuseiHp = kakuseiHp.replace(',','')
        idousokudo = idousokudo.replace(',','')
        reach = reach.replace(',','')
        dps = dps.replace(',','')
        kakuseiDps = kakuseiDps.replace(',','')
        shokiKougeki = shokiKougeki.replace(',','')
        saidaiKougeki = saidaiKougeki.replace(',','')
        kakuseiKougeki = kakuseiKougeki.replace(',','')
        kougekiKankaku = kougekiKankaku.replace(',','')
        toughness = toughness.replace(',','')
        sougouDps = sougouDps.replace(',','')
        kakuseiSougouDps = kakuseiSougouDps.replace(',','')
        
        name = name.replace(' ','')
        shusshin = shusshin.replace(' ','')
        nenrei = nenrei.replace(' ','')
        seibetsu = seibetsu.replace(' ','')
        rarelity = rarelity.replace(' ','')
        zokusei = zokusei.replace(' ','')
        seichouType = seichouType.replace(' ','')
        buki = buki.replace(' ','')
        bukiShubetsu = bukiShubetsu.replace(' ','')
        doujiKougekisuu = doujiKougekisuu.replace(' ','')
        kougekiDansuu = kougekiDansuu.replace(' ','')
        shokiHp = shokiHp.replace(' ','')
        saidaiHp = saidaiHp.replace(' ','')
        kakuseiHp = kakuseiHp.replace(' ','')
        idousokudo = idousokudo.replace(' ','')
        reach = reach.replace(' ','')
        dps = dps.replace(' ','')
        kakuseiDps = kakuseiDps.replace(' ','')
        shokiKougeki = shokiKougeki.replace(' ','')
        saidaiKougeki = saidaiKougeki.replace(' ','')
        kakuseiKougeki = kakuseiKougeki.replace(' ','')
        kougekiKankaku = kougekiKankaku.replace(' ','')
        toughness = toughness.replace(' ','')
        sougouDps = sougouDps.replace(' ','')
        kakuseiSougouDps = kakuseiSougouDps.replace(' ','')
        
        
        self.log('url: %s' % response.url)
        self.log('fileName: %s' % response.url)
        fileSavePath = filePath + name + '.csv'
        
        fileBody = "'名前','出身','年齢','性別','レア','属性','成長タイプ','武器','武器種別','同時攻撃数','攻撃段数','初期HP','最大HP','覚醒HP','移動速度','リーチ',"
        fileBody = fileBody + "'DPS','覚醒DPS','初期攻撃力','最大攻撃力','覚醒攻撃力','攻撃間隔','タフネス','総合DPS','覚醒総合DPS'"
        
        fileBody = fileBody + '\r\n' + name
        fileBody = fileBody + ',' + shusshin
        fileBody = fileBody + ',' + nenrei
        fileBody = fileBody + ',' + seibetsu
        fileBody = fileBody + ',' + rarelity
        fileBody = fileBody + ',' + zokusei
        
        fileBody = fileBody + ',' + seichouType
        fileBody = fileBody + ',' + buki
        fileBody = fileBody + ',' + bukiShubetsu
        fileBody = fileBody + ',' + doujiKougekisuu
        fileBody = fileBody + ',' + kougekiDansuu
        
        fileBody = fileBody + ',' + shokiHp
        fileBody = fileBody + ',' + saidaiHp
        fileBody = fileBody + ',' + kakuseiHp
        fileBody = fileBody + ',' + idousokudo
        fileBody = fileBody + ',' + reach
        fileBody = fileBody + ',' + dps
        fileBody = fileBody + ',' + kakuseiDps
        
        fileBody = fileBody + ',' + shokiKougeki
        fileBody = fileBody + ',' + saidaiKougeki
        fileBody = fileBody + ',' + kakuseiKougeki
        fileBody = fileBody + ',' + kougekiKankaku
        fileBody = fileBody + ',' + toughness
        fileBody = fileBody + ',' + sougouDps
        fileBody = fileBody + ',' + kakuseiSougouDps
        
        with open(fileSavePath, 'wb') as f:
            f.write(fileBody.encode(encoding='shift-jis'))
            f.close()
        self.log('Saved file %s' % fileSavePath)

