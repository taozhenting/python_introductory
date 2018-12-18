import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""
    def setUp(self):
        """创建实例供测试使用"""
        self.give_user = Employee('tao','zhenting')
    def test_give_default_raise(self):
        self.assertEqual(self.give_user.give_raise(),'taozhenting 5000')
    def test_give_custom_raise(self):
        self.assertEqual(self.give_user.give_raise(10000),'taozhenting 10000')

if __name__ == '__main__':
    unittest.main()