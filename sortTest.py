import random
from timeit import default_timer
from quicksort import quicksort
from mergesort import mergesort

def main():
    test_data = generate_random_list(10000)
    assert sorted_timed(test_data) == quicksort_timed(test_data) \
            == mergesort_timed(test_data)

def timer(f):
    def wrapper(*args, **kwargs):
        begin = default_timer()
        result = f(*args, **kwargs)
        end = default_timer()
        print(f"Function took {end - begin} seconds to compute.")
        return result
    return wrapper

@timer
def sorted_timed(*args, **kwargs):
    return sorted(*args, **kwargs)

@timer
def quicksort_timed(test_data, *args, **kwargs):
    n = len(test_data)
    return quicksort(test_data, 0, n)

@timer
def mergesort_timed(*args, **kwargs):
    return mergesort(*args, **kwargs)

def generate_random_list(length):
    return [random.randint(-100, 100) for _ in range(length)]


if __name__ == "__main__":
    main()
