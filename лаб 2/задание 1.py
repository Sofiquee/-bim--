
money_capital = 20000
salary = 5000
spend = 6000
increase = 1.05

month = 0
mani = 0

while money_capital > 0:
    mani = spend - salary
    money_capital -= mani
    spend *= increase
    if money_capital < 0:
        break
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)