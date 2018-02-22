#!/bin/bash

export PATH=$PATH:/usr/local/bin
cd /opt/scrapy/icisben

nohup scrapy crawl icisben >> icisben.log 2>&1 &