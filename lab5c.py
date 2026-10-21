# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Jude Flores
# Date: October 21st, 2026
# Purpose: Process File data.
# Usage: ./lab5c.py
with open("rhyme.txt", "w") as dataFile :
  dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")

with open("rhyme.txt", "r") as dataFile :
  line = dataFile.readline()
  while line != "":
    line = line.rstrip()
    words = len(line.split())
    print(line , "-----" , words , " words")
    line = dataFile.readline()

