from playLA.Vector import Vector
from playLA.GramSchmidtProcess import gram_schmidt_process


if __name__ == "__main__":

    basis1 = [Vector([2, 1]), Vector([1, 1])]
    res1 = gram_schmidt_process(basis1)
    for row in res1:
        print(row)
    res1 = [row / row.norm() for row in res1]
    for row in res1:
        print(row)
    print(res1[0].dot(res1[1]))

    basis2 = [Vector([2, 3]), Vector([4, 5])]
    res2 = gram_schmidt_process(basis2)
    for row in res2:
        print(row)
    res2 = [row / row.norm() for row in res2]
    for row in res2:
        print(row)
    print(res2[0].dot(res2[1]))

    basis3 = [Vector([1, 0, 1]), Vector([3, 1, 1]), Vector([-1, -1, -1])]
    res3 = gram_schmidt_process(basis3)
    for row in res3:
        print(row)
    res3 = [row / row.norm() for row in res3]
    for row in res3:
        print(row)
    print(res3[0].dot(res3[1]))
    print(res3[0].dot(res3[2]))
    print(res3[1].dot(res3[2]))

    basis4 = [Vector([1, 1, 5, 2]), Vector([-3, 3, 4, -2]), Vector([-1, -2, 2, 5])]
    res4 = gram_schmidt_process(basis4)
    for row in res4:
        print(row)
    res4 = [row / row.norm() for row in res4]
    for row in res4:
        print(row)
    print(res4[0].dot(res4[1]))
    print(res4[0].dot(res4[2]))
    print(res4[1].dot(res4[2]))


