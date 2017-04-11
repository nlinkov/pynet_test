#!/usr/bin/env python

from ciscoconfparse.ciscoconfparse import CiscoConfParse as CCP
from pprint import pprint as pp

with open('cisco_config.txt') as file:
   parse = CCP(file)

pp(parse.find_objects(r'crypto map CRYPTO'))
ff_parents = parse.find_objects(r'crypto map CRYPTO')

i = 0

while i < len(parents):
    print i
    print parents[i]
    i += 1
