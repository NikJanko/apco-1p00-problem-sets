
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

    # print(itr_fib(50))

def fix_me_2(list=[1, 3, 6, 5, 5]):
        # ps.display("rest")
        """
        reverse a list then print the reversed list. use insert and pop to do this
        
        error is one line, find and fix it.
        """
        arr = list
        for i in arr:
            arr.insert(i, arr.pop(-1))
            
        return arr

print(fix_me_2())
