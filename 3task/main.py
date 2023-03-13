summa = int(input("Введіть суму грошей, яку хочете покласти на депозит\n"))
months = int(input("На скільки місяців хочете покласти?\n"))
addition = int(input("Скільки грошей ви будете додавати кожного місяця?\n"))
percents = 15
tax = 18
war_collect = 1.5

mounth_cl = (((summa / 100) * 15) / 12) * months
fm_min_taxs = mounth_cl - (((mounth_cl / 100) * 18) + ((mounth_cl / 100) * 1.5))
total_summa_cl = summa * (1 + (15/100)) ** (1 / (12 / months))
total_summa = total_summa_cl - (((total_summa_cl / 100) * 18) + ((total_summa_cl / 100) * 1.5))

print(f"Зароблено за перший місяць: {fm_min_taxs}")
print(f"Всього було вкладено: {summa + (addition * (months - 1))}")
print(f"Дохід за весь період: {total_summa}")
