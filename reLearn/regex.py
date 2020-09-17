#!/usr/bin/python3

import re

pattern = re.compile('^From:.*')
print(re.search(pattern, "From: bob jones").group())
