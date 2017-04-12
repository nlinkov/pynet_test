#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
  ip_addr = '184.105.247.70'
  username = 'pyclass'
  password = '88newclass'

  remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
  output1 = remote_conn.read_until('sername:', TELNET_TIMEOUT)
  #print "output1: " + output1 + "end1"
  remote_conn.write(username + '\n')
  output2 = remote_conn.read_until('ssword:', TELNET_TIMEOUT)
  #print "output2: " + output2 + "end2"
  remote_conn.write(password + '\n')

  time.sleep(1)
  output3 = remote_conn.read_very_eager()
  #print "output3: " + output3 + "end3"
  
  remote_conn.close()
  #print "connection closed"

if __name__ == '__main__':
   main()
