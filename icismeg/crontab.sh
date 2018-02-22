#!/bin/bash

export PATH=$PATH:/usr/local/bin
cd /opt/scrapy/icis/icismeg

nohup scrapy crawl icismeg >> icismeg.log 2>&1 &