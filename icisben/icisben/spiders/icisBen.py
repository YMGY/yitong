#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

from scrapy import Spider, FormRequest, Request

from items import IcisBenItem


class icisMa(Spider):
    name = 'icisben'
    urlTemplate = 'https://dashboard.icis-china.com/Quote/FavouriteQuotes'
    homeUrl = 'https://dashboard.icis-china.com/'
    loginUrl = 'https://dashboard.icis-china.com/LogOn?ReturnUrl=%2f'
    cookies = {}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
        , 'referer': 'https://dashboard.icis-china.com'
        , 'Origin': 'https://dashboard.icis-china.com'
        , 'Accept-Language': 'zh-CN,zh:q=0.9'

    }  # 设置浏览器用户代理

    allowed_domains = ['dashboard.icis-china.com']

    def start_requests(self):
        yield Request(url=self.loginUrl,
                      meta={'cookiejar': 1},
                      headers=self.header,
                      callback=self.login)

    def login(self, response):
        formdata = {"UserName": "nanatang@cbichina.com", "Password": "20180207", "RememberMe": "true",
                    "LoginButton": "登录"}
        yield FormRequest.from_response(
            response=response,
            url=self.loginUrl,
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.header,
            formdata=formdata,
            callback=self.login_after,
        )

    def login_after(self, response):
        """登录后请求需要登录才能查看的页面，如个人中心，携带授权后的Cookie请求"""
        yield Request(
            url=self.homeUrl,
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.header,
            callback=self.parse_info
        )

    def parse_info(self, response):
        self.header.__setitem__('Accept', 'application/json,text/javascript,*/*,q=0.01')
        self.header.__setitem__('Accept-Encoding', 'gzip,deflate,br')
        self.header.__setitem__('X-Requested-With', 'XMLHttpRequest')
        scriptContents = response.xpath('//script[@type="text/javascript"]').extract()
        scriptData = scriptContents[0].split('\r\n')[1].split('=')[1]
        smData = json.loads(scriptData[0:-1])
        favouriteQuotes = smData['workspaceProfiles'][1]['quotation']['favouriteQuotes']

        # formData = {'quoteIds':"{i}icis-china/SM059",'quoteIds':"{i}icis-china/SM049"}
        postData = {}
        for id in favouriteQuotes:
            postData.__setitem__("quoteIds", id['seriesId'])
            yield FormRequest(
                url=self.urlTemplate,
                meta={'cookiejar': response.meta['cookiejar']},
                headers=self.header,
                formdata=postData,
                callback=self.parse
            )

    def parse(self, response):
        body = json.loads(response.body_as_unicode())
        if not body:
            return

        icisSmItem = IcisBenItem()
        for key in icisSmItem.fields:
            icisSmItem[key] = body['favouriteQuotations'][0][key]
        yield icisSmItem
