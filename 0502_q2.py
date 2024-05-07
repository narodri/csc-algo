s = input()
n = int(input())
a = input()

p = []
for t in range(100):
    p.append(0)

b = a.split()
for i in range(len(b)):
    p[i] = int(b[i])

for j in range(len(b)):
    s += " "
    while p[j]!=0:
        s += "a"
        p[j] -= 1

print(s)
