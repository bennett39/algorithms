import unittest

def reverse_slice(s):
    return s[::-1]


def reverse_iterative(s):
    ans = ""
    for c in s:
        ans = c + ans
    return ans


def reverse_recursive(s, tail=""):
    if not s:
        return tail
    tail += s[-1:]
    s = s[:-1]
    return reverse_recursive(s, tail)


class test_reverse(unittest.TestCase):
    def test_reverse_slice(self):
        result = reverse_slice("Python")
        self.assertEqual(result, "nohtyP")
    def test_reverse_slice_spaces(self):
        result = reverse_slice("Happy Birthday!")
        self.assertEqual(result, "!yadhtriB yppaH")

    def test_reverse_iterative(self):
        result = reverse_iterative("Python")
        self.assertEqual(result, "nohtyP")
    def test_reverse_iterative_spaces(self):
        result = reverse_iterative("Happy Birthday!")
        self.assertEqual(result, "!yadhtriB yppaH")

    def test_reverse_recursive(self):
        result = reverse_recursive("Python")
        self.assertEqual(result, "nohtyP")
    def test_reverse_recursive_spaces(self):
        result = reverse_recursive("Happy Birthday!")
        self.assertEqual(result, "!yadhtriB yppaH")


if __name__ == "__main__":
    unittest.main()
