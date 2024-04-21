# contest-pA
insert = input().split()
n = int(insert[0])
t = float(insert[1])
sum = 0
for i in range(n - 1):
    sum += int(input())
answer = sum * t / (n - t)
if (answer - int(answer)) < 0.5:
    print(int(answer))
else:
    print(int(answer) + 1)