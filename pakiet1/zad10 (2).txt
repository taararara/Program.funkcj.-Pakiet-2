def generator():
    x = 0
    while True:
        yield x
        x +=2

gen = generator()
pietnascie_pierwszych = [next(gen) for _ in range(15)]
print(pietnascie_pierwszych)
