# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов
# сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в
# два раза больше журавликов, чем Петя и Сережа вместе?

sum_crane = int(input('Введите количество сделанных журавликов: '))
child_kate = int((sum_crane / 3) * 2)
child_pete = int((child_kate / 2) / 2)
child_sergey = int(child_pete)
print(f'Катя сделала {child_kate}, Петя сделал {child_pete}, Сережа сделал {child_sergey}')