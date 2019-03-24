import numpy as np

if __name__ == "__main__":

    # 矩阵创建
    A = np.array([[1, 2], [3, 4]])
    print(A)

    # 矩阵的属性
    print(A.shape)
    print(A.T)

    # 获取矩阵的元素
    print(A[1, 1])
    print(A[0])
    print(A[:, 0])
    print(A[1])

    # 矩阵的基本计算
    B = np.array([[5, 6], [7, 8]])
    print(A + B)
    print(A - B)
    print(10 * A)
    print(A * B)  # 无意义
    print(A.dot(B))

    p = np.array([10, 100])
    print(A + p)

    print(A.dot(p))



