class Fib(object):
    def __init__(self, num):
        self.num = num

    def __len__(self):
        return self.num

    def __str__(self):
        a = []
        tmp = 0
        tmp_1 = 0
        tmp_2 = 1
        a.append(tmp_1)
        a.append(tmp_2)
        for i in range(self.num - 2):
            tmp = tmp_1
            tmp_1 = tmp_2
            tmp_2 = tmp + tmp_1
            a.append(tmp_2)
        return str(a)


f = Fib(10)
print(f)
print(len(f))


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        return '%s/%s' % (self.p, self.q)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)


class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):

    __slots__ = ('score',)

    def __init__(self, name, gender, score):
        super().__init__(name, gender)
        self.score = score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print(s.score)
