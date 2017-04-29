#!/usr/bin/env python

from snmp_helper3 import snmp_get_oid, print_or_error

def main():

  #snmp_version = '2c'
  snmp_credentials = ('test1', )
  snmp_socket = ('192.168.20.112', )
  snmp_oid = '1.3.6.1.2.1.1.1.0'
  snmp_security_level = ('sha', 'aes128')

  get_oid = snmp_get_oid(snmp_credentials, snmp_socket, snmp_oid, snmp_security_level)

  print "Trying: "
  print_or_error(get_oid)


if __name__ == '__main__':
   main()
