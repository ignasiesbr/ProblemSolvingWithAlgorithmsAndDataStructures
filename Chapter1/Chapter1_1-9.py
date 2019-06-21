#1. Implement the simple methods getNum and getDen
#2 Modify the constructor so GCD is used. Make the __add__ modifications
#3 Implement __sub__ , __mul__ , __truediv__
#4. Implement the operators gt,ge,lt,le
#5. Modify the constructor to check both num and den are int. Raise an excecption if not.
#6. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly
#7. __radd__
#8. __iadd__
#9. __repr__

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self,top,bottom):
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise TypeError
        else:
            common = gcd(top, bottom)
            self.num = top//common
            self.den = bottom//common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # __add__ without gcd, no longer neccesary
    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum,newden)

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    #Since addition is commutative,
    __radd__ = __add__

    def ___iadd__(self,other):
        return self.__add__(other)

    def __repr__(self):
        return "Fraction(" + str(self.num) + "," + str(self.den) + ")"



myFraction = Fraction(2,3)
















