"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True

print(is_prime(3))

def sum_odd(num):
    total_sum = 0
    i = 1
    if num < 1:
        return None
    
    while i <= num:
        if i % 2 == 1:
            total_sum += i
        else:
            print("num" , {i}, "is not odd")
    return total_sum

print(sum_odd(10))

    """
class MatrixM:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def store_matrix(self):
        storage_dict = {}
        key = 0
        for row in self.matrix:
            for col in row:
                if col != 0:
                    storage_dict[key] = col
                    key += 1
       # print(storage_dict)
        return storage_dict

    def add_matrix_dict(self, dict1, dict2):
        result = []
        for value1, value2 in zip(dict1.values(), dict2.values()):
            result.append(value1 + value2)
        return result

    def multiply_matrix_dict(self, dict1, dict2):
        result = []
        for value1, value2 in zip(dict1.values(), dict2.values()):
            result.append(value1 * value2)
        return result

matrixA = [
    [0,1,3],
    [0,5,0],
    [6,0,0]
]
matrixB = [
    [0,0,3],
    [0,7,0],
    [0,0,8]
]
inst1 = MatrixM(matrixA)
inst2 = MatrixM(matrixB)

dict1 = inst1.store_matrix()
dict2 = inst2.store_matrix()

print(dict1)
print(dict2)

#add_matrix_dict(dict1, dict2)
print(inst1.add_matrix_dict(dict1, dict2))
print(inst1.multiply_matrix_dict(dict1, dict2))


class MatrixM:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0
        self.storage = self.store_matrix()

    def store_matrix(self):
        storage_dict = {}
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val != 0:
                    storage_dict[(i, j)] = val
        return storage_dict

    def pretty_print(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(str(self.storage.get((i, j), 0)))
            print(" ".join(row))

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        
        result = {}
        result.update(self.storage)
        
        for (i, j), val in other.storage.items():
            result[(i, j)] = result.get((i, j), 0) + val
        
        return MatrixM(self.dict_to_matrix(result))

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix A's columns must equal Matrix B's rows")
        
        result = {}
        for (i, k), val_a in self.storage.items():
            for j in range(other.cols):
                if (k, j) in other.storage:
                    result[(i, j)] = result.get((i, j), 0) + val_a * other.storage[(k, j)]
        
        return MatrixM(self.dict_to_matrix(result, self.rows, other.cols))

    def dict_to_matrix(self, d, rows=None, cols=None):
        rows = rows or self.rows
        cols = cols or self.cols
        matrix = [[0]*cols for _ in range(rows)]
        for (i, j), val in d.items():
            matrix[i][j] = val
        return matrix



