#! /usr/bin/python
# -*- coding:utf-8 -*-

# using PyCrypto
# URL : https://www.dlitz.net/software/pycrypto/

from Crypto.Hash import MD5
h = MD5.new()
h.update('C:\INSIGHT\Accounting\Confidential\[Top-Secret]_2011_Financial_deals.xlsx|9296')
print h.hexdigest()

# output
# d3403b2653dbc16bbe1cfce53a417ab1
