import json
# Открываем JSON-файл
with open("sample-data.json") as file:
   data = json.load(file)
# Заголовок таблицы
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("=" * 90)
# Парсим и выводим данные
for item in data["imdata"]:
   attributes = item["l1PhysIf"]["attributes"]
   dn = attributes["dn"]
   description = attributes["descr"] if attributes["descr"] else "N/A"
   speed = attributes["speed"]
   mtu = attributes["mtu"]
   print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")