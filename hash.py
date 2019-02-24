#!/usr/bin/python
import hashlib
# python 2.7

to_hash = raw_input("Enter something for me to hash : ")

print(hashlib.sha256(to_hash).hexdigest())

