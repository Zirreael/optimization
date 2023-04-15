# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 20:11:01 2023

@author: user
"""

import unittest

from nelder_mead_2 import nelder_mead

class Test1(unittest.TestCase):
    
    def test_himmelblau(self):
        function = "(x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2"
        point = nelder_mead(2, 100, function)
        ans = point.coord
        x = round(ans[0], 2)
        y = round(ans[1], 2)
        if x>2 and x<3.3:
            self.assertEqual(x, 3)
            self.assertEqual(y, 2)
        if x<-2 and x>-3:
            self.assertEqual(x, -2.81)
            self.assertEqual(y, 3.13)
        if x<-3:
            self.assertEqual(x, -3.78)
            self.assertEqual(y, -3.28)
        if x> 3.3:
            self.assertEqual(x, 3.58)
            self.assertEqual(y, -1.85)
            
    def test_rosenbrock(self):
        function = "(1 - x) ** 2 + 100 * (y - x ** 2) ** 2"
        point = nelder_mead(2, 100, function)
        ans = point.coord
        x = round(ans[0], 2)
        y = round(ans[1], 2)
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)
        
    def test_but(self):
        function = "(x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2"
        point = nelder_mead(2, 100, function)
        ans = point.coord
        x = round(ans[0], 2)
        y = round(ans[1], 2)
        self.assertEqual(x, 1)
        self.assertEqual(y, 3)
        
        
def main():
    unittest.main()
    
main()