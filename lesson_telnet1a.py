#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
  ip_addr = '192.168.20.111'
  username = 'test'
  password = 'test'

  remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
  output1 = remote_conn.read_until('sername:', TELNET_TIMEOUT)
  print "output1: " + output1
  remote_conn.write(username + '\n')
  output2 = remote_conn.read_until('ssword:', TELNET_TIMEOUT)
  print "output2: " + output2
  remote_conn.write(password + '\n')

  time.sleep(1)
  output3 = remote_conn.read_very_eager()
  print "output3: " + output3

  remote_conn.write("terminal length 0" + '\n')
  time.sleep(1)
  output4 = remote_conn.read_very_eager()

  remote_conn.write("show version" + '\n')
  time.sleep(1)
  output5 = remote_conn.read_very_eager() 
 
  print "output5: " + output5

  remote_conn.close()
  print "connection closed"

if __name__ == '__main__':
   main()
