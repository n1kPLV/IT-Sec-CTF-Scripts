#!/usr/bin/env python3

import subprocess
from cProfile import run
from ftplib import FTP
import os
import re
from sys import stdout

p = re.compile(b'fl\{.*?\}')
user_patt = re.compile(b'\x0dUSER (.+?)\x0d\x0a')
pass_patt = re.compile(b'\x0dPASS (.+?)\x0d\x0a')

for i in range(101,140):
    # serverAdress = f"192.168.88.{i}"
    
    # ftp = FTP(serverAdress)
    # ftp.login()

    # os.mkdir(f'tmp/{i}')

    # with open(f'tmp/{i}/hiddensecret', 'wb') as fp:
    #   ftp.retrbinary('RETR hiddensecret', fp.write)
    #   fp.close()

    # ftp.quit()
    # f = open(f'tmp/{i}/hiddensecret', 'rb')

    # data = bytearray(f.read())

    # # quick patch
    # data[0x193c] = 0x90
    # data[0x193d] = 0x90

    # with open(f'tmp/{i}/hiddensecret_p', 'wb') as fp:
    #   fp.write(data)
    #   fp.close()

    os.chmod(f'tmp/{i}/hiddensecret_p', 0o777)
    print(f'-----------------{i}--------------')
    ps = subprocess.run(f'tmp/{i}/hiddensecret_p', input=b"1234567890")

    #output, errors = ps.

    #print(f"{i}: {user_patt.findall(f.read())}")
  