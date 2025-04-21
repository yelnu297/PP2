import psycopg2
import sys
import locale

print("Default encoding:", sys.getdefaultencoding())
print("Locale encoding:", locale.getpreferredencoding())

conn = psycopg2.connect(
    dbname="lab11",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)
print("Connection successful")
conn.close()
