def fizzbuzz(x, y, n):
    for i in range(1, n+1):
        if i % (x * y) == 0:
            print("Fizzbuzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz")
        else:
            print(i)

