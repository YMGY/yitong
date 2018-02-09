#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import re
import string

from scrapy import Spider, FormRequest, Request, Selector


class ccfDatePrice(Spider):
    name = 'ccfDatePrice'
    homeUrl = 'http://www.ccf.com.cn'
    loginUrl = 'http://www.ccf.com.cn/member/member.php'  # 登录页面

    # searchUrl = 'http://so.ccf.com.cn/Search?total_page=1&terms=%E5%8E%9F%E6%B2%B9%E7%9F%B3%E5%8C%96%E8%8A%B3%E7%83%83%E7%B1%BB'
    recycledfiberUrl = 'http://www.ccf.com.cn/informs/recycledfiber.html'
    cookies = {}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        # 'Accept-Language': 'zh-CN,zh:q=0.9',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Upgrade-Insecure-Requests': '1',
        # 'X-Powered-by': 'PHP/5.2.17'
    }  # 设置浏览器用户代理

    allowed_domains = ['www.ccf.com.cn']

    def start_requests(self):
        yield Request(url=self.loginUrl,
                      meta={'cookiejar': 1},
                      headers=self.header,
                      callback=self.login)

    def login(self, response):
        formdata = {
            'custlogin': '1',
            'url': '',
            'lng': '121.35127',
            'lat': '31.21978',
            # 's': '',
            'action': 'login',
            "username": "xinwangsh",
            "password": "20180207",
            "savecookie": "1",
            'imageField.x': '31',
            'imageField.y': '13'
        }
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
        self.header.__setitem__('Referer', self.recycledfiberUrl)
        yield Request(
            url=self.recycledfiberUrl,
            meta={'cookiejar': response.meta['cookiejar']},
            # headers=self.header,
            callback=self.parse_info
        )

    def parse_info(self, response):
        # self.header.__setitem__('Accept', 'application/json,text/javascript,*/*,q=0.01')
        # self.header.__setitem__('Accept-Encoding', 'gzip,deflate,br')
        # self.header.__setitem__('X-Requested-With', 'XMLHttpRequest')
        alist = response.xpath(
            '//div[@id="informsleft2015"]//div[@class="divleftwidth982015 tablegrayborderthree"]/div[@class="tabBox"]').extract()
        ## 取第二个div
        if len(alist) > 2:
            reportDiv = Selector(text=alist[1])
            chenReport=reportDiv.xpath('//div').extract()[7]
            chenReportSelector=Selector(text=chenReport).xpath('@//a').extract()
            for alink in chenReportSelector:
                print(alink)


        p1 = '原油石化芳烃类'

    def parse(self, response):
        body = json.loads(response.body_as_unicode())
        if not body:
            return
