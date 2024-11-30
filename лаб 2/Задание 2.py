salary = 5000
spend = 6000
months = 10
increase = 1.03
month = 10
mani = 0
money_capital = 0

while month > 0:
    mani = spend - salary
    money_capital += mani
    spend *= increase
    month -= 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))