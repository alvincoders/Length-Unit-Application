def name():
  name = input("Please enter your name:\n")
  print("Welcome %s to the Length Units Converter Application.\n" %name)
def menus():
  print("1. Enter 1 for Inches to Feet Conversion\n2. Enter 2 for Inches to Yards Conversion\n3. Enter 3 for Inches to Miles Conversion\n4. Enter 4 To Exit The Program\n")

def inchtofeet(inches):
  return (inches/12)
def inchtoyard(inches):
  return (inches/36)
def inchtomiles(inches):
  return (inches/63360)


def selection(operation,inches):
    if operation == 1:
      return "The distance in feet is %s feet\n" %inchtofeet(inches)
    elif operation == 2:
      return "The distance in yards is %s yards\n" %inchtoyard(inches)
    elif operation == 3:
      return "The distance in miles is %s miles\n" %inchtomiles(inches)
    elif operation == 4:
      quit


def main():
  operation = 0 
  name()
  while operation != 4:
    menus()
    operation = int(input("Input a choice from the menu\n"))
    if operation > 4 or operation < 1:
      print("That is not a valid option\n")
    elif operation != 4:
      inches = int(input("Enter your distance in inches\n"))
      result = selection(operation,inches)
      print(result)
    else: 
      print("Thank you for using the Length Units Converter Application")
    
main()