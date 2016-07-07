#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import os



URL = ('https://www.pararius.nl/library/app_getListHouses.php?lang=nl&cmd=1&version=1.1&cityname=Utrecht&range=5&delivery=3&nrBedrooms=3&m2=10&minPrice=0&maxPrice=1750&pageSize=100000&pageNr=1')

r = requests.get(URL)
parsed_json = json.loads(r.text)


#check for files
if not os.path.exists('huidig.txt'):
    open('huidig.txt', 'w').close()
if not os.path.exists('oud.txt'):
    open('oud.txt', 'w').close()

#open old one
file_huidig = open("huidig.txt", "r+")
x = str(file_huidig.read())
file_huidig.close()

#open new
file_old = open("oud.txt", "r+")
#nieuwe in de oude file plaatsen
file_old.write(x)
file_old.close()


#write new files to new txt
file_huidig = open("huidig.txt", "r+")
file_huidig.write(str(parsed_json))

#compare in other script
