from datetime import datetime, timedelta

noww = datetime.now()
print(f"Сейчас: {noww.strftime('%Y-%m-%d-%H-%M-%S-%f')}")