#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint as pp

config_dump = CiscoConfParse('cisco_config.txt')

ff_children = config_dump.find_objects(r'pfs group2')

for i in ff_children:
   if (i.is_child):
      print i.parent.text
      for j in i.parent.all_children:
         print j.text
   elif (i.is_parent):
      print i.text
      for j in i.all_children:
         print j.text
   else:
      pass
