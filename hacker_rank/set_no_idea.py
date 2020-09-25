n, m = input().split()
n=int(n)
m=int(m)
check = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness=0
for item in check:
    if (item in a):
        happiness += 1
    if (item in b):
            happiness -= 1
print(happiness)
