n = int(input().strip())
names = []
scores = []

for i in range(n):
    names.append(input().strip())
names.sort()

for i in range(n):
    score = 0
    for j in range(len(names[i])):
        score += (ord(names[i][j]) - 64)
    scores.append(score * (i + 1))

q = int(input().strip())

for i in range(q):
    name = input().strip()
    print(scores[names.index(name)])