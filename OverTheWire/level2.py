#!/usr/bin/env python
from pwn import *

shell = ssh('bandit2', 'bandit.labs.overthewire.org', password='rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi', port=2220)
flag = shell.cat('spaces\ in\ this\ filename')
print(flag)
