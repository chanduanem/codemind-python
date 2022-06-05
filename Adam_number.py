def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
a=int(input())
c=a**2
v=reverse(a)
p=reverse(v**2)
if c==p:
    print('True')
else:
    print('False')