#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:50:24 2017

@author: inoueshinichi
"""

import requests
url = "https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
    print (video['title']['$t'])
    