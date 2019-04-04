import numpy as np
from numpy.linalg import eig

if __name__ == "__main__":
    A1 = np.array([[4, -2],
                   [1, 1]])
    eigenvalues1, eig_en_vectors1 = eig(A1)
    print(eigenvalues1)
    print(eig_en_vectors1)
    print()

    # 关于y=x翻转
    A2 = np.array([[0, 1],
                   [1, 0]])
    eigenvalues2, eig_en_vectors2 = eig(A2)
    print(eigenvalues2)
    print(eig_en_vectors2)
    print()

    # 旋转90°
    A3 = np.array([[0, -1],
                   [1, 0]])
    eigenvalues3, eig_en_vectors3 = eig(A3)
    print(eigenvalues3)
    print(eig_en_vectors3)
    print()

    # 几何重数为1
    A4 = np.array([[3, 1],
                   [0, 3]])
    eigenvalues4, eig_en_vectors4 = eig(A4)
    print(eigenvalues4)
    print(eig_en_vectors4)
    print()
