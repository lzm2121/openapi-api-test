from mytry import degree
import unittest

class MytryTest(unittest.TestCase):
    def setUp(self) -> None:
        print(f'用例{self}开始执行')

    def test_youxiu(self):
        student = ('Cassies', 88)
        excepted = {'code': 0, 'msg': "优秀"}
        result = degree(*student)
        self.assertEqual(excepted, result)
        print(result)

    def test_jige(self):
        student = ('Cassies', 68)
        excepted = {'code': 0, 'msg': "合格"}
        result = degree(*student)
        self.assertEqual(excepted, result)

if __name__ == '__main__':
    unittest.main()
