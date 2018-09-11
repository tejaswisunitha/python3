arr=raw_input()
def largest(arr,n):
    max=arr[0]
    for i in range(1, n):
        if arr[i]>max:
            max=arr[i]
    return max
n=len(arr)
ans=largest(arr,n)
print (ans)
