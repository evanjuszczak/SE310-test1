import unittest
import math
team_name = "group 4"

def addition(number1, number2):
  print("We are adding " + str(number1) + " and " + str(number2))
  return number1 + number2

def multiplication (number1, number2):
  print ("We are multiplying " + str(number1) + " and " + str(number2))
  return number1 * number2

def calculator():
  print("Calculator by team =  " + team_name)
  print("Choose the operation you want to perform: ")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Integer Division")
  print("6. Square Root")
  print("7. Exponent")

  choice = int(input("Enter your choice: "))



calculator()

def division(number1, number2):
  print("We are dividing " + str(number1) + " and " + str(number2))
  return number1 / number2

def subtraction(number1, number2):
  print("We are subtraction " + str(number1) + " and " + str(number2))
  return number1 - number2

def IntegerDivision (number1, number2):
  print ("We are Integer Dividing " + str(number1) + " and " + str(number2))
  return number1 // number2

def SQRTredo(number1, number2):
  print("We are square rooting " + str(number1) + " and " + str(number2))
  return number1 ** number2

class TestMathEdgeCases(unittest.TestCase):

    # 1. Division by Zero
    def test_divide_by_zero(self):
        """Checks that dividing by zero raises a ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    # 2. Float Precision
    def test_float_precision(self):
        """
        Checks for precision issues (e.g., 0.1 + 0.2 != 0.3).
        Use assertAlmostEqual to handle tiny rounding differences.
        """
        result = 0.1 + 0.2
        # Standard assertEqual would fail here: 0.30000000000000004 != 0.3
        self.assertAlmostEqual(result, 0.3, places=7)

    # 3. Square Root of Negative Numbers
    def test_sqrt_negative_number(self):
        """Checks that sqrt of a negative number raises a ValueError."""
        with self.assertRaises(ValueError):
            square_root(-1)

if __name__ == '__main__':
    unittest.main()

