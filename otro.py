#! /usr/local/bin/python3
import sys

try:
  inp = sys.argv[1]
  lin = len(inp)
  print("Given: %s" % inp)
  print(" Even: %s" % inp[0:lin:2])
  print("  Odd: %s" % inp[1:lin:2])
except (IndexError, NameError):
  print("Gimme some")
