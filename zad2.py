from itertools import product
list1 = input("podaj litere pierwsza:"), input("podaj litere druga:")
list2 = input("podaj litere trzecia:"), input("podaj litere czwarta:")

kombinacja = list(product(list1, list2))
print(kombinacja)
