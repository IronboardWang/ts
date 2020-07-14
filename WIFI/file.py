def mul(*numbers):
    total = 1
    return [number * number  for number in numbers ]
print(mul(1,2,3,4))