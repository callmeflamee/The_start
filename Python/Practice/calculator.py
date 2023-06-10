OPS = ['+', '-', '*', '/']

def get_numbers():
    while True:

      num1 = input("Enter a number: ")

      try:
         num1 = int(num1)
      except ValueError:
         try:
            num1 = float(num1)
         except ValueError:
           print('Please enter a valid number!')
           continue
      
      operator = input("Enter the opreation to b performed (+,-,*,/): ")
      
      try:
         operator = str(operator)
      except ValueError:
         print("Please enter a valid operation!")
      
      if operator not in OPS:
         print('Please enter a valid operation (+,-,*,/)')
         continue
           
      num2 = input("Enter 2nd number: ")

      try:
         num2 = int(num2)
      except ValueError:
         try:
            num2 = float(num2)
         except ValueError:
           print('Please enter a valid number!')
           continue
      
      break
    return num1, operator, num2

def add(x, y):
   ans = x + y
   print(f"The sum of {x} and {y} is {ans}")
   return ans

def sub(x, y):
   ans = x - y
   print(f'The diffrence of {x} & {y} is {ans}')
   return ans

def multiply(x, y):
   ans = x * y
   print(f'The Multiplication of {x} & {y} is {ans}')
   return ans

def divide(x, y):
   if y == 0:
      print("Divison by zero is not allowed!")
   ans = x / y
   print(f'The division of {x} & {y} is {ans}')
   return ans


def main():
   x ,op, y = get_numbers()

   if op == '+':
      add(x,y)

   elif op == '*': 
      multiply(x,y)

   elif op == '/':
      divide(x,y)

   elif op == '-':
      sub(x,y)


   
main()

      
    