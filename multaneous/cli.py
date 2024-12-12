import argparse
def main():
  ps = argparse.ArgumentParser(prog="Multaneous", description="Multaneous help section", usage="%(prog)s [Option]")
  ps.add_argument("--version", action="store_true", help="Displays multaneous version")
  ps.add_argument("--math", action="store_true", help="A simple basic calculator")
  args = ps.parse_args()
  if args.version:
    print("version 0.0.1")
  elif args.math:
    math()
def math():
  try:
    num1 = int(input("Num1 >>> "))
    num2 = int(input("Num2 >>> "))
    operations = input("Operation (e.g +,-,*,/,**) >>> ")
    if operations == "+":
      r = num1 + num2
    elif operations == "-":
      r=num1 - num2
    elif operations == "*":
      r=num1 * num2
    elif operations == "/":
      if num2 != 0:
        r=num1 / num2
      else:
        print("Zero division is not allowed")
        return
    elif operations == "**":
      r=num1 ** num2
    else:
      print("Invalid Operator")
      return
    print(r)
  except ValueError:
    print("Invalid input, please remove any symbols or letters.")
