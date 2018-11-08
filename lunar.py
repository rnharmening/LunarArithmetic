from itertools import zip_longest

class Lunar:

    def __init__(self, val = 0):
        self.value = val

    def __add__(self, other):
        a, b = self.value, other.value
        a, b = (str(a), str(b)) if a > b else (str(b), str(a))
        # b = ''.join("0" for _ in range(len(a)-len(b))) + b

        c = a[:len(a)-len(b)] + ''.join(x if x > y else y for x, y in zip(a[::-1], b[::-1]))[::-1]

        return Lunar(int(c))

    # TODO not done yet
    def __mul__(self, other):
        a, b = self.value, other.value
        a, b = (str(a), str(b)) if a > b else (str(b), str(a))
        res = Lunar(0)
        for i, b_ in enumerate(str(b[::-1])):
            c = Lunar(int(a[:len(a)-len(b)]
                      + ''.join(x if x < y else y for x, y in zip(a[::-1], b_[::-1]))[::-1]
                      + ''.join("0" for _ in range(i))))
            res += c

        return res

    def __str__(self):
        return str(self.value)



x, y = Lunar(115), Lunar(115)

print(x + y)
print(x * y)