#!/bin/bash

export PATH=$PATH:/usr/local/bin
cd /opt/scrapy/ccf

nohup scrapy crawl ccfDatePrice >> ccfDatePrice.log 2>&1 &