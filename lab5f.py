# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Jude Flores
# Date: October 21st, 2026
# Purpose: Catch ZeroDivisionError
# Usage: ./lab5f.py
def safe_divide(a,b):
  # divide a by b
  # Add an exception block to raise the error if error occurs because of a zero denominator.
  # Except block should display the appropriate error messages
  try:
    quotient = int(a) / int(b)
    print(quotient)
  except ZeroDivisionError:
    print("You cannot divide by zero")


def main():
  safe_divide(10,5)  # works
  safe_divide(10,0)  # exception : Zero Division Erclearor

if __name__ == "__main__" : 
  main()
