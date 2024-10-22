

from random import randrange

def get_int_between_1_10():
    return randrange(1, 10)

class Matrix:

    def __init__(self):
        self.__my_id = get_int_between_1_10()

    def __str__(self) -> str:
        return '0'

    def __repr__(self) -> str:
        return '1'





def several_zeros():
    return 1

def several_zeros_custom(nb_zeros):
    mylist = []
    # for myitem in mylist:
    #     print(myitem)
    for i in range(nb_zeros):
        mylist.append(0)
    return mylist

def matrix(rows, cols):
    matrix = [
        [1, 4],
        [9, 5],
        [2, 8]
    ]
    return matrix

if __name__ == '__main__':
    result_matrix = matrix(0, 0)
    print(result_matrix)
    print(result_matrix[1])
    row1 = result_matrix[1]
    print(type(result_matrix[1]))
    print(row1[1])
    print(row1)
    for row in result_matrix:
        for col in row:
            print(col)
        