import pymysql


class MysqlOperate():
    """连接数据库，并进行操作"""

    def __init__(self):
        self.cnn = pymysql.connect(host='localhost', port=3306, user='root', passwd='SaveElement', charset='utf8')
        self.cursor = self.cnn.cursor()

    def db_close(self):
        self.cursor.close()  # 关闭游标
        self.cnn.close()  # 关闭数据连接

    def db_execute(self, sql):
        """执行sql语句并提交：包含增、删、改"""
        try:
            print('执行的sql语句为：', sql)
            self.cursor.execute(sql)
            self.cnn.commit()
        except Exception as e:
            self.cnn.rollback()
            print('sql语句执行错误，进行回滚')

    def db_select(self, sql):
        """执行查询sql语句，并返回所有查询结果"""
        try:
            print("查询sql语言为：", sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print('查询失败')


if __name__ == '__main__':





    sql = "SELECT * FROM inventory.type"


    connect = MysqlOperate()
    data = connect.db_select(sql)

    for iterm in data:
        print(iterm)

    connect.db_close()
