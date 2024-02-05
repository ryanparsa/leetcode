import timeit


def fib_v1(n: int):
    p1 = 0
    p2 = 1
    for i in range(n):
        p1, p2 = p2, p1 + p2

    return p1


def fib_v2(n: int):
    if n in {0, 1}:
        return n

    return fib_v2(n - 1) + fib_v2(n - 2)


state = {
    0: 0,
    1: 1,
}


def fib_v3(n: int):
    if n not in state:
        state[n] = fib_v3(n - 1) + fib_v3(n - 2)
    return state[n]


def fib_v4(n: int):
    stack = [(0, 1)]

    for i in range(n):
        x, y = stack.pop()

        stack.append((y, x + y))

    return stack[0][0]


print("fib_v1(30)", timeit.timeit("fib_v1(30)", setup="from __main__ import fib_v1", number=100))
print("fib_v2(30)", timeit.timeit("fib_v2(30)", setup="from __main__ import fib_v2", number=100))
print("fib_v3(30)", timeit.timeit("fib_v3(30)", setup="from __main__ import fib_v3", number=100))
print("fib_v4(30)", timeit.timeit("fib_v4(30)", setup="from __main__ import fib_v4", number=100))
