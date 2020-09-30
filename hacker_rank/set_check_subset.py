for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())

A=set(map(int,"1 2 3 5 6".split()))
B=set(map(int,"9 8 5 6 3 2 1 4 7".split()))
print(A.intersection(B)==A)
