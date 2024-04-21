n = int(input())
max_score = n * 5
score = 0.0
keys = ["AC", "WA", "TLE", "RE", "--"]
values = [5, 3, 0, 0, 0]
table = dict(zip(keys, values))

def late(score, time):
    return max(score * (1 - time / 24), 0)

for i in range(n):
    problem = input().split()
    if problem[3] != "--":
        score += late(table[problem[2]], int(problem[3]))

print(f"{round(score)}/{max_score}")
