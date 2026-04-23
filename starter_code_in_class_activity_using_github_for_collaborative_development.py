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

class TestMathOperations(unittest.TestCase):

    def test_add_valid_numbers(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, -1), -2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            add(10, "5")

    def test_missing_input_arguments(self):
        with self.assertRaises(TypeError):
            add(10)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            add(None, 5)

if __name__ == '__main__':
    unittest.main()

