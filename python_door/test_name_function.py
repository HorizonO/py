import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """能够正确地处理想Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name,'Janis Joplin')
unittest.main()