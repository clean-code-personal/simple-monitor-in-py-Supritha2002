import unittest
from check_limits import *

class TestBattery(unittest.TestCase):
    
    def test_battery_condition(self):
        self.assertTrue(battery_is_ok(25,'Celcius', 70, 0.7,'german'))
        self.assertFalse(battery_is_ok(120,'fahrenheit', 75, 0,'english'))

if __name__ == '__main__':
    unittest.main()
