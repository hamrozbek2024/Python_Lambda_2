# 11
print(list(map(lambda x: x*2, [1, 2, 3, 4])))

# 12
print(list(filter(lambda x: x % 3 == 0, [3, 5, 6, 9, 10])))

# 13
print(list(map(lambda x: int(x**0.5), [4, 9, 16])))

# 14
print(sorted([(1, 3), (2, 1), (4, 2)], key=lambda x: x[1]))

# 15
print(list(filter(lambda s: len(s) > 4, ["hi", "hello", "world"])))

# 16
print(list(map(lambda x: x+5 if x > 10 else x-5, [5, 15, 20])))

# 17
print(sorted([5, -2, 9, -1], key=lambda x: abs(x)))

# 18
print(list(map(lambda x: str(x)*2, [1, 2, 3])))

# 19
print(list(filter(lambda x: x.isdigit(), ["12", "ab", "34", "7x"])))

# 20
print(list(map(lambda x: x % 2 == 0, [1, 2, 3, 4])))
