
n = int(input())


d = []

print(d)

for i in range(n):
    d.append(input().split())

date = []

for i in range(n):
    temp = d[i].pop(1)
    date.append([temp])

print(n,d, date)

print(len(d[0]))