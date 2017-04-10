#!/usr/bin/env python

import yaml
import json

my_list = range(8)
my_list.append('whatever')
my_list.append('something')
my_list.append({})
my_list[-1]['ip_addr'] = '1.1.1.1'
my_list[-1]['dev_name'] = 'rtr01'
my_list[-1]['attributes'] = range(5)

with open('test6_write.yaml', "w") as file:
   file.write(yaml.dump(my_list, default_flow_style=False))

with open('test6_write2.yaml', "w") as file:
   file.write(yaml.dump(my_list, default_flow_style=True))

with open('test6_write.json', "w") as file:
   file.write(json.dumps(my_list))
