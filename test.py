import math
import unittest
from random import random
import random


from xunit_testing import function_def
class Testing(unittest.TestCase):
    def test_dividing_by_zero(self):
       try:
           function_def(0)
       except:
           print('В знаменателе 0. Нельзя продолжить')
    def test_general_function(self):
       y = function_def(random.uniform(0, math.pi * 1/2))
       self.assertEqual('Функция выполнима',y)
    def test_general_function1(self):
       y = function_def(random.uniform(math.pi * 1/2, math.pi))
       self.assertEqual('Функция выполнима',y)
    def test_general_function2(self):
       y = function_def(random.uniform(math.pi , math.pi*3/2))
       self.assertEqual('Функция выполнима',y)
    def test_general_function3(self):
       y = function_def(random.uniform(math.pi*3/2 , math.pi*2))
       self.assertEqual('Функция выполнима',y)
