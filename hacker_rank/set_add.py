country=set()

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        country.add(input().strip())

print(len(country))
