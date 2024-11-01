salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

cash = 0

for i in range(1, months+1):
    cash = cash + salary
    cash = cash - spend
    spend = spend * (1 + increase)

if cash != int(cash):
    salary_airbag = int(0 - cash) + 1
else:
    salary_airbag = int(0 - cash)

# столько не хватило денег, чтобы не влезать в долги!

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", salary_airbag)
