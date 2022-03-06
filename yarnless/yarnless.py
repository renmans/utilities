#!/usr/bin/env python3

import re
import sys

regex = r".*Exception(:|;) (.*)$"
with sys.stdin as stdin:
    for line in stdin:
        match = re.search(regex, line)
        print(match.group(2)) if match else None
