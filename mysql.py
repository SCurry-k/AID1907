'''
mysql操作数据基本流程
'''
import pymysql
db = pymysql.connect(host='localhost',
                     port= 3306,
                     user='root',
                     password='123456',
                     database='books',
                     charset='utf8')

# 获取游标 (操作数据库 执行sql语句 得到执行结果)
cur = db.cursor()

# 执行sql语句

sql = "insert into book values (7,'全职高手','蝴蝶蓝',435,'2011-2-28','奇书网','网游天才叶不修');"

cur.execute(sql)

cur.commit()

