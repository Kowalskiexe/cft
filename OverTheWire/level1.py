#!/usr/bin/env python
from pwn import *

shell = ssh('bandit1', 'bandit.labs.overthewire.org', password='NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL', port=2220)
flag = shell.cat('./-')
print(flag)
