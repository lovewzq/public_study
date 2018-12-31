import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='python')
cur = conn.cursor()

sql = "select * from ip"
cur.execute(sql)
conn.close()