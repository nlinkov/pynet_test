#!/usr/bin/env python

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
  cmd = cmd.rstrip()
  remote_conn.write(cmd + '\n')
  time.sleep(1)
  return remote_conn.read_very_eager()

def login(remote_conn, username, password):
  output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
  remote_conn.write(username + '\n')
  output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
  remote_conn.write(password + '\n')
  return output

def connection(ip_addr, port = 23, timeout = 6):
  try :
     return telnetlib.Telnet(ip_addr, port, timeout)
  except socket.timeout:
     sys.exit("Connection timed out!")

def main():
  ip_addr = '192.168.20.111'
  username = 'test'
  password = 'test'

  remote_conn = connection(ip_addr)

  output = login(remote_conn, username, password)
  print output
  
  output = send_command(remote_conn, 'terminal length 0')
  print output

  output = send_command(remote_conn, 'show version')
  print output

  remote_conn.close()
  #print "connection closed"

if __name__ == '__main__':
   main()
