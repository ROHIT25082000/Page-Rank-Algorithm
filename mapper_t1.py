#!/usr/bin/env python3
import sys
from_word = ""

for line in sys.stdin:
	line = line.strip()
	if line[0] != "#":
		from_word,b = line.split("\t",1)

		print(from_word,"\t",b)

