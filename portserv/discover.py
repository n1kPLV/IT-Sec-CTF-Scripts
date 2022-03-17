#!/usr/bin/env python3

from socket import SHUT_RDWR, create_connection
from time import sleep
import re

p = re.compile('fl\{.*\}')

timeouts = [101,105,106,107,108,109,117,119,121,133,136]

for i in range(101,140):
  serverAdress = f"192.168.88.{i}"
  for portno in range(8003,9000):
    try:
      sock = create_connection((serverAdress, portno))
      sock.settimeout(10)

      #attack1 = b"128\n"
      #attack2 = b"aaaa"

      #sock.sendall(attack1)
      #sock.sendall(attack2)

      try:
        res = sock.recv(4096)

        print(f"{i}: {res} at port {portno}")
      except:
        print(f"{i}: timeout")

      sock.close()
    except:
      pass