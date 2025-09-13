num = int(input())
max_num = num
count = 1
while num != 0:
    if num > max_num:
        max_num = num
        count = 1
    elif num == max_num:
        count += 1
    num=int(input())
print(count)

"""
a = list(map(int, input().split()))
print(a.count(max(a)))
"""
