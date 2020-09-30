if __name__ == '__main__':
    n = int(input())
    A = set(input().split())
    k = int(input())
    l4=input()
    l5 = set(input().split())
    l6 = input()
    l7 = set(input().split())
    l8 = input()
    l9 = set(input().split())
    l8 = input()
    l11 = set(input().split())

A.intersection_update(A,l5)
A.update(A,l7)
A.symmetric_difference_update(l9)
A.difference_update(l11)
A=map(int, A)
print(sum(A))


