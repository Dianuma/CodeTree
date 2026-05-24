X, Y = map(int, input().split())

# Please write your code here.
ans = set()

for n in range(len(str(X)), len(str(Y)) + 1):
    for a in '0123456789':
        for b in '0123456789':
            if a != b:
                for i in range(n):
                    s = a * i + b + a * (n - i - 1)
                    if s[0] != '0' and X <= int(s) <= Y:
                        ans.add(s)

print(len(ans))