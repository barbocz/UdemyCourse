arr = map(int, "57 57 -57 57".split())
print(arr)
n=4
# for i in arr:
#     print(i)

sorted_arr=sorted(arr)
max=sorted_arr[n-1]

for i in range(n-1,-1,-1):
    if (sorted_arr[i]<max):
        print (sorted_arr[i])
        break

