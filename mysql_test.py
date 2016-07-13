# git clone https://github.com/PyMySQL/PyMySQL.git
# python setup.py install

import pymysql

con = pymysql.connect(host='localhost',
                      user='root',
                      password='root',
                      db='test',
                      charset='utf8')

cur = con.cursor()

try:
    row = cur.execute("insert into user values(NULL,'abc',11,'shanghai pudong',now())")
    print(row)
    con.commit()
except:
    con.rollback()

print("=" * 50)

row = cur.execute("select name from user order by rand() limit 1")
print(cur.fetchone())

print("=" * 50)

rows = cur.execute("select * from user")
for row in cur.fetchall() :
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print("=" * 50)

cur.close()
con.close()