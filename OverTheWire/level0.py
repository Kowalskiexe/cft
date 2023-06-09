#!/usr/bin/env python
from pwn import *

shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)
flag = shell.cat('readme')
print(flag)
