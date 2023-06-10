import unittest
def add_num(a,b):
  return a+b

class CalculatorTests(unittest.TestCase):
  def test_add(self):
    result = add_num(7,3)
    self.assertEqual(result, 10)

if __name__ == "__main__":
   unittest.main()
