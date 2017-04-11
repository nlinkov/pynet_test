#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint as pp
import re

config_dump = CiscoConfParse('cisco_config.txt')

ff_objects = config_dump.find_objects_wo_child(r'crypto map CRYPTO', 'AES')

for i in ff_objects:
   if (i.is_child):
      print i.parent.text
      for j in i.parent.all_children:
         if (re.search('transform-set', j.text) != None): 
            print j.text
         else:
            pass
   elif (i.is_parent):
      print i.text
      for j in i.all_children:
        if (re.search('transform-set', j.text) != None):
            print j.text
        else:
             pass
   else:
      pass
