#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.

numbers = []
summ1 = 0
summ2 = 0
for i in range (1, 1001):
    if i % 2 != 0:
        numbers.append(i ** 3)


for idx in range(len(numbers)):
    numb_summ = 0
    c = numbers[idx]
    while c:
        numb_summ += c % 10
        c = c // 10
    if numb_summ % 7 == 0:
        summ1 += numbers[idx]

    numbers[idx] += 17
    numb_summ = 0
    c = numbers[idx]
    while c:
        numb_summ += c % 10
        c = c // 10
    if numb_summ % 7 == 0:
        summ2 += numbers[idx]
print(list(numbers))
print(summ1)
print(summ2)
