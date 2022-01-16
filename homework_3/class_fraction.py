from dataclasses import dataclass

@dataclass(init=True, repr=False)
class Fraction():

    numerator : int = 1
    denominator : int = 1

    def __repr__(self) -> str:
        if self.denominator < 0 or self.numerator < 0:
            return f'Дробь вида : - {abs(self.numerator)}/{abs(self.denominator)}\
                Числитель = {self.numerator} | Знаменатель = {self.denominator}'
        return f'Дробь вида : {self.numerator}/{self.denominator}\
            Числитель = {self.numerator} | Знаменатель = {self.denominator}'
    
    def input_fraction(self):
        self.numerator, self.denominator = int(input()), int(input())
        assert self.denominator != 0
        if self.denominator < 0 and self.numerator < 0:
            self.numerator *= -1
            self.denominator *= -1
        return Fraction(self.numerator, self.denominator)
