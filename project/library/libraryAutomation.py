import sqlite3
db = sqlite3.connect("libraryDB.db")
cursor = db.cursor()
cursor.execute("""select * from users""")
uyeler = cursor.fetchall()
sayac = 0
for uye in uyeler:
 print(uye)
 sayac+=1
print(sayac)
db.commit()
db.close()