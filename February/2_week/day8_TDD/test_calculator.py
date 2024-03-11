import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(3,8)
        self.assertEqual(result,11)
    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(3,8)
        self.assertEqual(result,24)
    def test_devide(self):
        result = devide(10,2)
        self.assertEqual(result,5)

# 수학 함수 테스트
class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)

# 문자열 반전 함수 테스트       
class TestStringFunctions(unittest.TestCase):
    def test_reverse_string(self):
        result = reverse_string('likelion')
        self.assertEqual(result,'noilekil')

# 리스트 정렬 함수
class TestListFunctions(unittest.TestCase):
    def test_sort_list(self):
        result = sort_list(['James','Daniel','Smith','Karrot'])
        self.assertEqual(result,['Daniel','James','Karrot','Smith'])

# 사용자 정의 클래스 메서드 테스트
class TestPersonClass(unittest.TestCase):
    def test_is_adult(self):
        adult = Person('Scarlett',18)
        self.assertTrue(adult.is_adult())

# 예외 발생 테스트
class TestException(unittest.TestLoader):
    def test_exception(self):
        with self.assertRaises(ValueError):
            divide_new(10,0)

# 파일 처리 함수 테스트
class TestFileOperations(unittest.TestCase):
    def test_write_to_file(self):
        write_to_file('test.txt','Hello world')
        with open('test.txt','r') as f:
            self.assertEqual(f.read(),'Hello world')
if __name__ == "__main__":
    unittest.main()