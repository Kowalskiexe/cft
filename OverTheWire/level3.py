#!/usr/bin/env python
from pwn import *

shell = ssh('bandit3', 'bandit.labs.overthewire.org', password='aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG', port=2220)
flag = shell.cat('inhere/.hidden')
print(flag)
