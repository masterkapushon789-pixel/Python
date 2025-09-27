start_sum = int(input('начальная сумма > '))
percent = int(input('процентная ставка вклада > '))
target_sum = int(input('целевая сумма вклада > '))
m = 0
while start_sum < target_sum:
    start_sum += start_sum * (percent / 100) / 12
    m += 1
    print(f'{m} - {start_sum:.2f}')
