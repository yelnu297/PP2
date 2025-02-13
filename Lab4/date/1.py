from datetime import datetime, timedelta

noww = datetime.now()

nazad5 = noww - timedelta(days=5)

print(f"Сейчас: {noww.strftime('%Y-%m-%d')}")
print(f"5 дней назад: {nazad5.strftime('%Y-%m-%d')}")