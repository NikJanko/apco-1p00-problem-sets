
def factorial(n):
    fact = 1
    for i in range(1, 13):
        fact *= i
    print(fact)


def rec_prestep(phi, tolerance):
    tol = 10 ** (-tolerance)
    print(f"Using tolerance: {tol}")

    def rec(phi, tolerance):
        if abs(phi - 1.61803398875) < tolerance:
            return phi
        else:
            print(f"Current phi: {phi}")
            return rec(1 + 1/phi, tolerance)

    return rec(phi, tol)

# print(rec_prestep(1.0, 3))


def itr_fib(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b

print(itr_fib(50))