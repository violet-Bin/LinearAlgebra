from playLA.Matrix import Matrix

if __name__ == "__main__":

    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)

    print("matrix.shape() = {}".format(matrix.shape()))
    print("matrix.size() = {}".format(matrix.size()))
    print("len(matrix) = {}".format(len(matrix)))
    print("matrix[0, 1] = {}".format(matrix[0, 1]))
    print("matrix[0] = {}".format(matrix.row_vector(0)))
    print("matrix[0] = {}".format(matrix.col_vector(0)))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print("add:  {}".format(matrix + matrix2))
    print("sub:  {}".format(matrix2 - matrix))
    print("matrix * 2 =  {}".format(matrix * 2))
    print("2 * matrix = {}".format(2 * matrix))
    print("matrix / 2 = {}".format(matrix / 2))
    print("zero3 = {}".format(Matrix.zero(3, 3)))



