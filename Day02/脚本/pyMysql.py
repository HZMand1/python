#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.50.23", "root", "password", "aip_dev")

# 使用cursor()创建一个游标对象cursor
cursor = db.cursor()

# 使用 execute() 执行SQL查询
cursor.execute("SELECT * FROM `ap_app_comand`")

# 使用fetchall() 方法获取所有数据
data = cursor.fetchall()

# 打印数据
print(data)

# 关闭数据源
db.close()

# 关闭游标
cursor.close()