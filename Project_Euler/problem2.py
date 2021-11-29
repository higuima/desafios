value_a, value_b = 1, 2
result = []
while value_a < 4_000_000:
    if (value_a % 2 == 0):
        result.append(value_a)
    value = value_a + value_b
    value_a = value_b
    value_b = value

print(sum(result))