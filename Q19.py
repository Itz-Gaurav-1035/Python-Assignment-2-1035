x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)          # True (same object in memory)
print("x is z:", x is z)          # False (different objects with same content)
print("x is not z:", x is not z)  # True