from collections import Counter

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
print(max(Counter((a+b)//2 for i, a in enumerate(A) for b in A[i+1:] if (a+b)%2==0).values(), default=0))