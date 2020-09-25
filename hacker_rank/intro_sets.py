def average(heights):
    # heights_string="161 182 161 154 176 170 167 171 170 174"
    hs=set(map(int, heights))
    print(sum(hs) / len(hs))


if __name__ == '__main__':
    n = int(input())
    average(input().split())



