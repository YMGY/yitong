#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy import cmdline

name = 'icismeg'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())