#!/usr/bin/env python

from snmp_helper2 import snmp_get_oid_v3, snmp_get_oid_v2c, print_or_error

def main():
  community_string = 'test'
  snmp_user = 'test'
  auth_key = 'Test1234'
  priv_key = 'Test1234'
  snmp_device = '192.168.20.112'
  snmp_port=161
  auth_proto='sha'
  priv_proto='aes128'
  oid = '1.3.6.1.2.1.1.1.0'

  snmp_credentials_v3 = (snmp_user, auth_key, priv_key)
  snmp_credentials_v2c = (community_string)
  snmp_security_level = (auth_proto, priv_proto)
  snmp_socket = (snmp_device, snmp_port)


  get_oid = snmp_get_oid_v2c(snmp_credentials_v2c, snmp_socket, oid)
  
  print "First trying v2c: "
  print_or_error(get_oid)

  get_oid = snmp_get_oid_v3(snmp_credentials_v3, snmp_socket, snmp_security_level, oid)

  print "Trying v3: "
  print_or_error(get_oid)


if __name__ == '__main__':
   main()
