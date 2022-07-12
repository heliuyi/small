# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_db.py
# @Time      :2022-05-02 22:29
# @Author    :DongWenFei
'''
1.数据库连接 conn cur
2.获取一条数据？
3.获取条数
4.获取所有的数据
5.关闭数据库连接
'''
from Common.handle_configs import conf
import pymysql
class HandleDB:
    def __init__(self,database):
        #1.连接如数据库
        self.conn = pymysql.connect(
            host=conf.get('mysqls_fanxing','host'),
            port=conf.getint('mysqls_fanxing','port'),
            user=conf.get('mysqls_fanxing','user'),
            password=conf.get('mysqls_fanxing','password'),
            database=database,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
            # 列表嵌套字典形式输出
        )
        self.cur=self.conn.cursor()#2.创建游标

    def select_one_data(self,sql):
        '''

        :param sql:
        :return:返回字典类型
        '''
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all_data(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self,sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def update(self,sql):
        '''
        对数据库进行增，删，改的操作
        :param sql:
        :return:
        '''
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    #pass

    # sql="SELECT * FROM promote_activity LIMIT 10"
    # result=HandleDB().select_one_data(sql)
    sql = "SELECT id FROM `promote_activity` WHERE promote_type=3 and `status`=1"
    result=HandleDB().select_all_data(sql)
    print(result)
    #print(result[1]['id'])

    a=[]
    for i in result:
        a.append(str(i['id']))
    print(a)

'''
    操作数据库的类封装
    1、在init创建一个连接对象
    2、封装一个获取sql查询完之后，查询集中所有数据的方法
    3、封装一个获取sql查询完之后，查询集中第一条数据的方法
    4、封装一个获取sql查询完之后，查询到的数据条数
注意点：
在工作中项目中如果涉及到多个数据库，封装的时候init
方法中数据库的配置就不要从配置文件中直接读（应该参数化处理）
'''


    # import json
    # #result=json.loads(lists)
    # #print(type(lists))
    #
    # print(lists)
    # print(lists[0]["reg_name"])#列表取值

    #print(lists['reg_name'])#字典取值

