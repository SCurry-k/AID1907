import pymysql

db = pymysql.connect(host='localhost',
                     port= 3306,
                     user='root',
                     password='123456',
                     database='books',
                     charset='utf8')

cur= db.cursor()

# 执行语句
with open('image','rb') as f:
    data = f.read()

sql = 'insert into images values '
cur.execute(sql,data)
db.commit()

cur.close()