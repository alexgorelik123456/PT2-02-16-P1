#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re

my_input_list = sys.argv[1:]

#convert list to string
my_string=''.join(my_input_list)

#delete excess whitespace
my_string = re.sub(r'\s+', ' ', my_string)

#delete symbols
print re.findall('[a-z]', my_string)

