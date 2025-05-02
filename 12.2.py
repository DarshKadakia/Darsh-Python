class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        return [[self.matrix[i][j] + other.matrix[i][j] for j in range(3)] for i in range(3)]

    def multiply(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def transpose(self):
        return [[self.matrix[j][i] for j in range(3)] for i in range(3)]
