from datetime import datetime, timedelta
import math
a = input_datetime = input("Введите дату в формате YYYY-MM-DD: ")
b = input_datetime = input("Введите дату в формате YYYY-MM-DD: ")
c = abs(datetime.strptime(a, '%Y-%m-%d') - datetime.strptime(b, '%Y-%m-%d'))
otvet = c.days*24*60*60
print(f"Разница между датами: {otvet} секунд")
