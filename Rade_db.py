'''
rade_db   pymysql  读操作演示
'''

import pymysql

# 链接数据库
db = pymysql.connect(user='root',
                     passwd='123456',
                     database='books',
                     charset='utf8')

# 获取游标
cur = db.cursor()

# 获取数据
sql = "select * from book where title='甄嬛传';"

cur.execute(sql)

# 遍历游标
# for i in cur:
#     print(i)

# 获取所有查询结果
# all_row = cur.fetchall()
# print(all_row)

# 获取多个查询结果
# many_row = cur.fetchmany(2)
# print(many_row)

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)