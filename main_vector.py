from playLA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    print(vec)
    print(vec.__len__())
    print("vec[0]={}, vec[1]={}".format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    vec3 = Vector([-1, 2])
    print("+{} = {}".format(vec, +vec3))
    print("-{} = {}".format(vec, -vec3))

    zero2 = Vector.zero(2)
    print(zero2)
    print("{} + {} = {}".format(vec, zero2, vec + zero2))

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))

    print("normalize {} is {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())
    print("normalize {} is {}".format(vec2, vec2.normalize()))
    print(vec2.normalize().norm())

    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}.".format(zero2))

    # try:
    print(vec.dot(vec2))
    # except

    vec4 = Vector([0, 0])
    print("{} == {} ? {}".format(zero2, vec4, vec4 == zero2))
    print("{} == {} ? {}".format(zero2, vec, vec == zero2))



