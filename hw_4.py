"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


def search_in_matrix(matrix, target):
    """
    The function searches for a number in a matrix. It returns [-1, -1] if the number isn't found/ list is empty,
    and the indeces if the number can be found in the matrix.

    Parameter: matrix, list of lists of numbers to carry the search on
    Parameter: target, aim number that we need to find out
    """
    result_counter = []
    row_counter = -1
    for item in matrix:
        row_counter +=1
        for i in item:
            if i == target:
                column = item.index(i)
                result_counter.extend([row_counter, column])
                return result_counter
    else:
        return [-1, -1]


# Test Cases

# Case 1. Result [3, 3]
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 44
print(search_in_matrix(matrix, target))

########################################################

# Case 2. Result [-1, -1]
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 66
print(search_in_matrix(matrix, target))

########################################################

# Case 3. Result [-1, -1]
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 0
print(search_in_matrix(matrix, target))

########################################################

# Case 4. Result [-1, -1]
matrix = [ ]

target = 44
print(search_in_matrix(matrix, target))

########################################################

# Case 5. Result [4, 5]
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 1004
print(search_in_matrix(matrix, target))

########################################################

# Case 6. Result [0, 0]
matrix = [
[1,4,7,12,15,1000]
]

target = 1
print(search_in_matrix(matrix, target))

########################################################

# Case 7. Result [-1, -1]
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = -44
print(search_in_matrix(matrix, target))


if __name__ == '__main__':
    search_in_matrix(matrix, target)