def fib(n):
    result = []
    for i in range(n):
        if i < 2:
            result.append(1)
        else:
            result.append(result[i-1] + result[i-2])
        yield result[-1]
