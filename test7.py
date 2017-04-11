#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

with open('test6_write.yaml') as file:
   my_list_y = yaml.load(file)

with open('test6_write2.yaml') as file:
   my_list_y2 = yaml.load(file)

with open('test6_write.json') as file:
   my_list_j = json.load(file)

print "my_list_y"
pp(my_list_y)

print "my_list_y2"
pp(my_list_y2)

print "my_list_j"
pp(my_list_j)
