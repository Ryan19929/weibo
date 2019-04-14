#!/user/bin/python
# -*- coding: utf-8 -*-
"""
@author: yhj
@time: 2018/10/14 13:19
@desc: 导入数据到数据库
"""

import codecs
from PycharmProjects.test1.mysql import mysql_operate


column_map = {u"用户id": "usr_id", u"微博内容": "content"}


def insert_data(conn):
    cursor = conn.cursor()
    fp = codecs.open("../result.txt", "r", encoding="utf-8")
    insert_data = dict()
    for line in fp:
        line = line.strip()  # 去掉换行等前后空白符
        if line == "":
            inser_sql = mysql_operate.add_sql("pachong", **insert_data)
            cursor.execute(inser_sql)
            insert_data.clear()
        else:
            key, value = line.split(":", 1)
            if key == u"用户id" or key == u"微博内容":
                value = value.split(";")[0]
            insert_data[column_map[key]] = value
    conn.commit()



if __name__ == '__main__':
    conn = mysql_operate.connection_sql("test1", host='127.0.0.1', user='root', passwd='1234', port=3306, charset='utf8')
    insert_data(conn)
    mysql_operate.close_sql(conn)