def whatDay(y, m, d):
    if m < 3:
        m += 12
        y -= 1
    k = y % 100
    j = y // 100
    h = (d + 13 * (m + 1) / 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return int(h)


t = int(input().strip())
for i in range(t):
    y1, m1, d1 = input().strip().split(' ')
    y1, m1, d1 = [int(y1), int(m1), int(d1)]
    y2, m2, d2 = input().strip().split(' ')
    y2, m2, d2 = [int(y2), int(m2), int(d2)]
    y = y1
    m = m1
    count = 0

    if d1 > 1:
        if m1 == 12:
            m = 1
            y += 1
        else:
            m += 1
    while y <= y2:
        while m <= 12:
            if whatDay(y, m, 1) == 1:
                count += 1
            if y == y2 and m == m2:
                break
            m += 1
        m = 1
        y += 1
    print(count)