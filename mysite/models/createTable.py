from mysite.models.mysqlOperate import MysqlOperate


class CreateTable():

    def __init__(self):
        self.mysqlOperate = MysqlOperate()


    def createTableType(self):
        """
        在数据库inventory中创建表单type
        :id: 分类编号（自增列）
        :type: 分类名字
        :comment: 备注信息
        """

        sql = "CREATE TABLE `inventory`.`type` " \
                          "(`id` INT NOT NULL AUTO_INCREMENT," \
                          "`type` TEXT(40) NULL," \
                          "`comment` TEXT(200) NULL,PRIMARY KEY (`id`));"

        self.mysqlOperate.db_execute(sql)


    def createTableInventory(self):
        sql = "CREATE TABLE `inventory`.`inventory` " \
                               "(`id` INT NOT NULL AUTO_INCREMENT," \
                               "`goods` TEXT(40) NULL," \
                               "`type` TEXT(40) NULL," \
                               "`num` INT NULL," \
                               "`comment` TEXT(600) NULL,PRIMARY KEY (`id`));"
        self.mysqlOperate.db_execute(sql)



    def createTableInbound(self):
        sql = "CREATE TABLE `inventory`.`inbound` " \
                               "(`id` INT NOT NULL AUTO_INCREMENT," \
                               "`goods` TEXT(40) NULL," \
                               "`inbound_num` INT NULL," \
                               "`inbound_date` INT NULL," \
                               "`comment` TEXT(600) NULL,PRIMARY KEY (`id`));"
        self.mysqlOperate.db_execute(sql)

    def createTableWarning(self):
        sql = "CREATE TABLE `inventory`.`warning` " \
                               "(`id` INT NOT NULL AUTO_INCREMENT," \
                               "`goods` TEXT(40) NULL," \
                               "`warning_num` INT NULL," \
                               "`comment` TEXT(600) NULL,PRIMARY KEY (`id`));"
        self.mysqlOperate.db_execute(sql)


    def createTableOutbound(self):
        sql = "CREATE TABLE `inventory`.`outbound` " \
                               "(`id` INT NOT NULL AUTO_INCREMENT," \
                               "`goods` TEXT(40) NULL," \
                               "`outbound_num` INT NULL," \
                               "`outbound_date` INT NULL," \
                               "`comment` TEXT(600) NULL,PRIMARY KEY (`id`));"
        self.mysqlOperate.db_execute(sql)


if __name__ == '__main__':

    createTable = CreateTable()
    createTable.createTableInbound()
    createTable.createTableOutbound()
    createTable.createTableWarning()






