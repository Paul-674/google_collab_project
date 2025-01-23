def add(x, y):
  """Adds two numbers together."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers.
     Returns an error message if the divisor is 0.
  """
  if y == 0:
    return "Division by zero error!"
  else:
    return x / y
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
  result = add(num1, num2)
elif operation == '-':
  result = subtract(num1, num2)
elif operation == '*':
  result = multiply(num1, num2)
elif operation == '/':
  result = divide(num1, num2)
else:
  result = "Invalid operation"
print(f"Result: {result}")