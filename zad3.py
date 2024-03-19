def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
cziag = fibonacci()
p_10_liczb = [next(cziag) for _ in range(10)]
print(p_10_liczb)