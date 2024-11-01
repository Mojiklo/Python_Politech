money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
cash = money_capital
count =0
while cash >= 0:

    cash = cash + salary - spend
    spend = spend * (increase + 1)
    count += 1

count -= 1


print("Количество месяцев, которое можно протянуть без долгов:", count)

