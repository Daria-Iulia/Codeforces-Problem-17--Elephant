length = (1, 2, 3, 4, 5)
x = int(input())

steps = 0
remaining = x
for step in sorted(length, reverse=True):
    while remaining >= step:
        remaining -= step
        steps += 1

print(steps)
                