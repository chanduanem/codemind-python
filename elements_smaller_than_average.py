x=int(input())
lst=list(map(int,input().split()))
avg=sum(lst)/x
c=0
for ele in lst:
    if ele<=avg:
        c+=1
print(c)