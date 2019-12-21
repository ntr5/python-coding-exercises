"""
[
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]
"""

def manual_incrementing_matrix(num):
    # create a matrix of num x num
    matrix = [ [ None for y in range(num) ] for x in range(num) ]

    counter = 0

    for idx, el in enumerate(matrix):
        for nested_idx, nested_el in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx

        counter += 1

    return matrix

print(manual_incrementing_matrix(5))

