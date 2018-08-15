# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:01:56 2018

@author: bittdy
"""

import re

raw_output = b"never { /* G(goods->Xdepot)&&G(depot->Xgoods)&&(G(!b)&&G(!door||open)) */accept_init : /* init */}"
 
never_regx  = re.compile(r"never \{ /\*(?P<formula>.+)\*/")

match = never_regx.find(raw_output)