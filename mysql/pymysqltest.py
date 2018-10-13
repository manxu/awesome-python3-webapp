import pymysql
conn = pymysql.Connect(host='192.168.99.100', port=3306, user='root', passwd='123456', db='activiti_api', charset='utf8')
cursor = conn.cursor()
sql ="select * from ai_user"
cursor.execute(sql)
print(cursor.rowcount)
rs = cursor.fetchone()
print(rs)

for each in cursor.fetchall():
    print(each[0])
