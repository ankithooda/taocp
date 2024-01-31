class LinearRandomGen():
    
def get_next(x0):
    m = 10              # Modulus
    a = 7               # Multiplier
    c = 7               # increment
    return ((a * x0 + c) % m)

def gen_random_seq(n):
    x = 7
    for i in range(100):
        x = get_next(x)
        print(x, end=', ')

