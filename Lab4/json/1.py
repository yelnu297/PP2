import json

with open("sample-data.json") as file:
   data = json.load(file)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("=" * 90)
for item in data["imdata"]:
   attributes = item["l1PhysIf"]["attributes"]
   dn = attributes["dn"]
   description = attributes["descr"] if attributes["descr"] else "N/A"
   speed = attributes["speed"]
   mtu = attributes["mtu"]
   print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")