def fizzbuzz(x, y, n):
    """ Prints fizz for factors of x and buzz for factors of y in range
    n. Prints fizzbuzz when factor of both x and y.
    Otherwise prints the number.
    """
    for i in range(1, n):
        if i % (x*y) == 0:
            print("fizzbuzz", end=", ")
        elif i % x == 0:
            print("fizz", end=", ")
        elif i % y == 0:
            print("buzz", end=", ")
        else:
            print(i, end=", ")
    print()

fizzbuzz(3, 4, 20)
fizzbuzz(3, 5, 20)
fizzbuzz(2, 5, 20)
