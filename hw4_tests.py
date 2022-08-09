import unittest
from hw_4 import search_in_matrix

test_matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

class TestCorrectIndices(unittest.TestCase):

    #  Number is in matrix: any number that can be found in the matrix variable, should return the indexes of the number
    def test_number_in_matrix(self):
        result = search_in_matrix(test_matrix, 44)
        self.assertEqual(result, [3, 3])

    #  Number is not in matrix: any number that cannot be found in the matrix variable, should return [-1, -1]
    def test_number_not_in_matrix(self):
        result = search_in_matrix(test_matrix, 66)
        self.assertEqual(result, [-1, -1])

    #  Number is last in matrix: last number in the matrix variable, should return the indexes for the number
    def test_number_last_in_matrix(self):
        result = search_in_matrix(test_matrix, 1004)
        self.assertEqual(result, [4, 5])

    #  Number is first in matrix and matrix has only have one list: last number in the matrix variable,
    #  should return the indexes for the number
    def test_number_first_in_matrix(self):
        result = search_in_matrix([[1,4,7,12,15,1000]], 1)
        self.assertEqual(result, [0, 0])

    #  Target is 0: should return [-1, -1]
    def test_number_is_zero(self):
        result = search_in_matrix(test_matrix, 0)
        self.assertEqual(result, [-1, -1])

    #  Variable Matrix is empty: any number, should return [-1, -1]
    def test_matrix_is_empty(self):
        result = search_in_matrix([], 44)
        self.assertEqual(result, [-1, -1])

    #  Number is in matrix but negative: any negative number number, should return [-1, -1]
    def test_negative_number(self):
        result = search_in_matrix(test_matrix, -44)
        self.assertEqual(result, [-1, -1])


if __name__ == '__main__':
    unittest.main()
