#
# A very simple subnet calculator in Python, written by
# Oscar Holst (https://github.com/oscarholst)
# Heavily inspired by Jack-Benny Persson's subnect calculator in C.
# Released under GNU GPLv2
#

import math

net = input('Enter netmask in slash-notation without the slash: ')

net = int(net)
if net >= 0 and net <= 32:
    addr = math.pow(2, 32 - net)
    addr = int(addr)
    print('Total addresses available: ', addr)

    # Check and set usable hosts to zero if it's a negative value
    hosts = addr - 2
    if hosts < 0:
        hosts = 0
    print('Usable addresses for host', hosts)

else:
    print('Only accepting input value between 0-32...')
