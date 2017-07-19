#! /usr/local/bin/python3
import sys

try:
  even = sys.argv[1]
  odd  = sys.argv[2]
  print("  Even: %s" % even)
  print("   Odd: %s" % odd)
  whole = ''.join((even[i] + odd[i]) for i in range(0,len(odd)))
  if len(odd) < len(even):
    whole = whole + even[len(even)-1]

  print("Result: %s" % whole)
except (IndexError, NameError):
  print("Gimme double some")
