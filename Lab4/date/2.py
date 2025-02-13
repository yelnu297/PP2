from datetime import datetime, timedelta

noww = datetime.now()
yesterday = noww - timedelta(days=1)
tomorrow = noww + timedelta(days=1)

print(yesterday.strftime('%Y-%m-%d'))
print(noww.strftime('%Y-%m-%d'))
print(tomorrow.strftime('%Y-%m-%d'))