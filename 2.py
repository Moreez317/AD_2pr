n = int(input())
counter = n
res = []

for i in range(n):
    for a in range(i):
        if counter != 0:
            res.append(i)
            counter = counter - 1

print(*res)