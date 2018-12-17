import unittest
from city_functions import get_city_country
class NamesTestCase(unittest.TestCase):
    """测试city_funcitions"""
    def test_city_country_name(self):
        """能够正确地处理像Santiago Chile"""
        formatted_name = get_city_country('santiago','chile',population='500000')
        self.assertEqual(formatted_name,'Santiago, Chile500000')

if __name__ == '__main__':
    unittest.main()