if __name__ == '__main__':
    n1 = int(input())
    s1=set(map(int, input().split()))

    n2 = int(input())
    s2=set(map(int, input().split()))
d1=s1.difference(s2)
d2=s2.difference(s1)
for i in (sorted(d1.union(d2))):
    print(i)
