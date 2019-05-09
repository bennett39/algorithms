def odds(m, n):
    """ Prints all odd numbers in range m - n. """
    if not m & 1:
        m += 1
    for i in range(m, n+1, 2):
        print(i)

odds(0, 10)
odds(20, 35)
