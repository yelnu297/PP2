import datetime
noww = datetime.datetime.now()
nazad5 = noww - datetime.timedelta(days=5)

print(f"Сейчас: {noww.strftime('%Y-%m-%d')}")
print(f"5 дней назад: {nazad5.strftime('%Y-%m-%d')}")