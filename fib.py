def fibonacci(n):
    last, curr = 1, 1
    for i in range(2, n):
        last, curr = curr, last + curr
    return curr

def main():
    while True:
        n = input("Provide an int: ")
        try:
            n = int(n)
            if n > 0:
                print(f"The {n}th Fibonacci number is: {fibonacci(n)}.")
            else:
                raise Exception
        except:
            print("Provide a valid input.")

if __name__ == "__main__":
    main()
