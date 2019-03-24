product = 1

while True:
    i = input("Provide an integer: ")
    try:
        i = int(i)
        product *= i
        print(product)
    except:
        print("Invalid input. Try again.")
