#!/usr/bin/env python3.8
from math import pi
from os import getenv

numdigits = int(getenv('DIGITS', 10))

print("%.*f" % (numdigits, pi))
