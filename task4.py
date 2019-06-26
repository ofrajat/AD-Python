#!usr/bin/python3

import os 
import crypt

x=input("Enter Anything:")
y="test"

if type(x)==type(y):
    password ="123  "
    encPass = crypt.crypt(password,"22")
    os.system("useradd -p "+encPass+" john")
