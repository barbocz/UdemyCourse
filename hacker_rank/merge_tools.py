def merge_the_tools(string, k):

    for i in range (0,len(string),k):
        work=string[i:i+k]
        result=""
        for j in range (0,len(work)):
            if (work[j] not in result):
                result=result+work[j]
                # print (work[j])
        print(result)

if __name__ == '__main__':
    # string, k = input(), int(input())
    string="AABCAAADA"
    k=3
    merge_the_tools(string, k)