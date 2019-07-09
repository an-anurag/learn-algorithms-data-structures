
class Fraction:
    """
    A class which will return fraction object such as 3/4 along with their operations
    """
    def __init__(self, numa, numb):
        self.num = numa
        self.den = numb

    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    @staticmethod
    def gcd_calculator(a, b):
        if a == 0:
            return b
        return Fraction.gcd_calculator(b % a, a)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * self.num
        new_den = self.den * other.den
        common = self.gcd_calculator(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __eq__(self, other):
        fist_num = self.num * other.den
        second_num = other.num * self.den
        return fist_num == second_num

    def __mul__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __sub__(self, other):
        pass


example = Fraction(25, 5)
example2 = Fraction(45, 8)
add = example + example2
print(example == example2)
print(add)
print(example)
print(example2)
add = example.__add__(example2)
print(add)


