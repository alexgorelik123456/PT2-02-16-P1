#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

def get_hash_md5_sum(filename):
    with open(filename, 'r') as f:
        m = hashlib.md5()
        while True:
            data = f.read(128)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

print(get_hash_md5_sum('file1.txt'))
print(get_hash_md5_sum('file2.txt'))

f1sum = get_hash_md5_sum('file1.txt')
f2sum = get_hash_md5_sum('file2.txt')

if f1sum == f2sum:
    print ('good job')
else:
    print ('bad job')
