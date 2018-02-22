#!/bin/bash

export PATH=$PATH:/usr/local/bin
cd /opt/scrapy/icis/icissm

nohup scrapy crawl icissm >> icissm.log 2>&1 &