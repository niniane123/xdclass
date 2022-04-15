import unittest
from unittest import TestCase
import junit_test as unit_test


class Test_my_test(TestCase):
    def test_my_add(self):
        test = unit_test.my_test()
        self.assertEqual(test.my_add(1, 5), 6)


# 开始执行单元测试
if __name__ == "__main__":
    unittest.main()
