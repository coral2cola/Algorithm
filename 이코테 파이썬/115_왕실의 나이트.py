n = input()

cnt = 0

row = n[0]  # a~h
col = n[1]  # 1~8

if ord(row) - 2 >= 97:
    if int(col) - 1 >= 1:
        cnt += 1
    if int(col) + 1 <= 8:
        cnt += 1

if ord(row) + 2 <= 104:
    if int(col) - 1 >= 1:
        cnt += 1
    if int(col) + 1 <= 8:
        cnt += 1

if int(col) - 2 >= 1:
    if ord(row) - 1 >= 97:
        cnt += 1
    if ord(row) + 1 <= 104:
        cnt += 1

if int(col) + 2 <= 8:
    if ord(row) - 1 >= 97:
        cnt += 1
    if ord(row) + 1 <= 104:
        cnt += 1

print(cnt)
