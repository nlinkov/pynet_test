#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint as pp

config_dump = CiscoConfParse('cisco_config.txt')

ff_parents = config_dump.find_objects(r'crypto map CRYPTO')

for i in ff_parents:
   print i.text
   for j in i.all_children:
      print j.text


