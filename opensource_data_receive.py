import pymysql

class SQL :
    def __init__(self, host='192.168.137.172', user='ssu', password='',
                 db='ssudb', charset='utf8'):
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          db=db,
                                          charset=charset)
        self.cursor = self.connection.cursor()
    def test(self) :
        try:
            query = "UPDATE data_table SET data=98 WHERE seat_number=0 AND name='Soongsil Univ';"
            print(query)
            self.cursor.execute(query)
            self.connection.commit()

        except Exception as e :
            print(str(e))
        
        
    def insert(self, table, *values):
        try:
            query = "INSERT INTO "+table+" VALUES ({}, {}, {},{});".format(*values)
            print(query)
            self.cursor.execute(query)
            self.connection.commit()

        except Exception as e :
            print(str(e))

    def update(self, table, value1,value2, *conds):
        try:
            query = "UPDATE "+table+" SET remainedtime={},cond={}".format(value1,value2)
            query += " WHERE seat_number={} AND name={};".format(*conds)
            print(query)
            self.cursor.execute(query)
            self.connection.commit()

        except Exception as e :
            print(str(e))

    def delete(self, table, *conds):
        try:
            query = "DELETE FROM "+table
            query += " WHERE seat_number={} AND name={};".format(*conds)
            print(query)
            self.cursor.execute(query)
            self.connection.commit()

        except Exception as e :
            print(str(e))

    def select(self, table):
        try:
            query = "SELECT * FROM "+table+";"
            self.cursor.execute(query)
            return self.cursor.fetchone()

        except Exception as e :
            print(str(e))

    def select_where(self, table, where):
        try:
            query = "SELECT * FROM {} WHERE {};".format(table, where)
            self.cursor.execute(query)
            return self.cursor.fetchone()

        except Exception as e :
            print(str(e))
