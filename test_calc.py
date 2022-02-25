import unittest
import calc

class testCalc(unittest.TestCase):
    def test_add(self):
        #result = calc.add(5,5)
        self.assertEqual(calc.add(5,5),10)
        self.assertEqual(calc.add(-5,5),0)
        self.assertEqual(calc.add(-5,-5),-10)
    
    def test_subtract(self):
        #result = calc.add(5,5)
        self.assertEqual(calc.subtract(5,5),0)
        self.assertEqual(calc.subtract(-5,5),-10)
        self.assertEqual(calc.subtract(-5,-5),-0)
        
    def test_multiply(self):
        #result = calc.add(5,5)
        self.assertEqual(calc.multiply(5,5),25)
        self.assertEqual(calc.multiply(-5,5),-25)
        self.assertEqual(calc.multiply(-5,-5),25)
        
    
    def test_divide(self):
        #result = calc.add(5,5)
        self.assertEqual(calc.divide(5,5),1)
        self.assertEqual(calc.divide(-5,5),-1)
        self.assertEqual(calc.divide(8,2),4)
        self.assertEqual(calc.divide(8,0),4)

        
        
        
        

if __name__ == "__main__":
    unittest.main()
        
    