list_a = [100.0, 200.0, -10.0]
list_b = [False, False, True]

for val_a, val_b in zip(list_a, list_b):
    print(val_a, val_b)

for index, val in enumerate(zip(list_a, list_b)):
    print(index, val)
