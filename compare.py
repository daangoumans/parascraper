#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from difflib import Differ


#open old
file_huidig = open("huidig.txt", "r")
#open new
file_old = open("oud.txt", "r")

#get files
huidig = file_huidig.read()
oud = file_old.read()

#sort function
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


#sort and compare, then print
if (ordered(huidig) == ordered(oud)):
    #same
    print('no new house')
else:
    #different
    print('new house')
