#!/bin/bash

export PATH=$PATH:/usr/local/bin
cd /opt/scrapy/icis/icisma

nohup scrapy crawl icisma >> icisma.log 2>&1 &