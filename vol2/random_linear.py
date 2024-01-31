class LinearRandomGen():

    def __init__(self, m, a, c, x):
        self.m = m     # Modulus
        self.a = a     # Multiplier
        self.c = c     # increment
        self.x = x

    def next(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

def gen_random_seq(n):

    random = LinearRandomGen(10, 7, 7, 7)

    for i in range(n):
        x = random.next()
        print(x, end=', ')

gen_random_seq(100)
