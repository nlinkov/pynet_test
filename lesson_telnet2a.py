#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6
  
def remote_cmd(remote_conn, cmd):
  cmd = cmd.rstrip()
  remote_conn.write(cmd + '\n')
  time.sleep(1)
  return remote_conn.read_very_eager()

def remote_login(remote_conn, username, password):
  #username = username.rstrip()
  #password = password.rstrip()
  remote_conn.read_until('sername:', TELNET_TIMEOUT)
  remote_conn.write(username + '\n')
  remote_conn.read_until('ssword:', TELNET_TIMEOUT)
  remote_conn.write(password + '\n')
  time.sleep(1)
  return remote_conn.read_very_eager()

def remote_connection(ip_addr, port, timeout):
  return telnetlib.Telnet(ip_addr, port, timeout)

def main():
  ip_addr = '192.168.20.111'
  username = 'test'
  password = 'test'

  remote_conn = remote_connection(ip_addr, TELNET_PORT, TELNET_TIMEOUT) 

  output3 = remote_login(remote_conn, username, password)
  print output3 

  output4 = remote_cmd(remote_conn, 'terminal length 0') 
  print output4

  output5 = remote_cmd(remote_conn, 'show version')
  print output5

  remote_conn.close()
  print "connection closed"

if __name__ == '__main__':
   main()
