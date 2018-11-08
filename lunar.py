from itertools import zip_longest

class Lunar:

    def __init__(self, val = 0):
        self.value = val

    def __add__(self, other):
        a, b = self.value, other.value
        a, b = (str(a), str(b)) if a > b else (str(b), str(a))

        c = a[:len(a)-len(b)] + ''.join(x if x > y else y for x, y in zip(a[::-1], b[::-1]))[::-1]

        return Lunar(int(c))

    def __mul__(self, other):
        a, b = self.value, other.value
        a, b = (str(a), str(b)) if a > b else (str(b), str(a))
        res = Lunar(0)
        for i, b_ in enumerate(str(b[::-1])):
            c = Lunar(int(''.join(x if x < b_ else b_ for x in a) + ''.join("0" for _ in range(i))))
            res += c

        return res

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':

    x, y = Lunar(9), Lunar(158)

    print(x + y)
    print(x * y)