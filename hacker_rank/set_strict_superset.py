
A, n, B, C =  set(input().split()), input(), set(input().split()),set(input().split())
#
#
# A=set("1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78".split())
# B=set("1 2 3 4 5".split())
# C=set("100 11 12".split())

print(B.intersection(A)==B and len(A.difference(B))>0)
