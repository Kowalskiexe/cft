#!/usr/bin/env python
from pwn import *

shell = ssh('bandit4', 'bandit.labs.overthewire.org', password='2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe', port=2220)
sh = shell.run('bash')
for i in range(10):
    file = f'inhere/-file0{i}'
    cmd = f'file -b {file}'.encode('ASCII')
    sh.sendline(cmd)
    sh.recvuntil(b'\r', timeout=1) # consume prompt
    file_type = sh.recvline(timeout=1)
    if file_type == b'ASCII text\n':
        sh.sendline(f'cat {file}'.encode('ASCII'))
        sh.recvuntil(b'\r', timeout=1) # consume prompt
        flag = sh.recvline(timeout=1)
        print(flag)
        break
