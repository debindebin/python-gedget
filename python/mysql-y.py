 # -*- coding: utf-8 -*-

import pymysql
 
# 打开数据库连接
db = pymysql.connect(host="rdsm7f0883mxww26597zo.mysql.rds.aliyuncs.com",port =3307,user= "xuebuapp", password="YiYi2017@WSX", database="iyuenr", charset='utf8' )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 查询语句
sql = "select id  from skill  where (first_agent_rate >0 or second_agent_rate>0)  and visibleFlag =1 and delFlag =0  and categoryId =102";
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      skillid = row[0]
       # 打印结果
      print (skillid)
      insertSql="insert into act_invite  (skill_id,type,app_define_id) values (%d,3,0)" % skillid
      cursor.execute(insertSql)
      db.commit()
except:
   print ("Error: unable to fetch data")
   db.rollback()
 
# 关闭数据库连接
db.close()