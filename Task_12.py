# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он
# задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введите S(сумма): '))
p = int(input('Введите P(произведение): '))
result = []
for i in range(s + p):
    if i == (s * i - p)**0.5:
        result.append(i)
print(*result if len(result) == 2 else result + result)
