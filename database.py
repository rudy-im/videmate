import sqlite3


class DB:

    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()

        self.cursor.execute('PRAGMA foreign_keys = ON;')


    def drop_table(self, name):
        self.cursor.execute('DROP TABLE IF EXISTS ' + name + ';')
        self.conn.commit()


    # cols : ['col_name DATA_TYPE CONSTRAINTS', ... ]
    def create_table(self, name, cols):
        if len(cols)<=0:
            return
        
        sql = 'CREATE TABLE ' + name + '('
        
        for col in cols:
            sql += col + ', '
        
        sql = sql[:-2]
        sql += ');'
        
        self.cursor.execute(sql)
        self.conn.commit()


    def get_col_names(self, tablename):
        self.cursor.execute('PRAGMA table_info(' + tablename + ')')
        columns = self.cursor.fetchall()
        column_names = [col[1] for col in columns]
        return column_names


    # values should be in order of the columns
    def insert(self, tablename, values):
        if len(values)<=0:
            return

        col_names = self.get_col_names(tablename)

        sql = 'INSERT INTO ' + tablename + '('

        for col_name in col_names:
            sql += col_name + ', '
        
        sql = sql[:-2]
        sql += ') VALUES ('

        for i in range(len(values)):
            sql += '?, '

        sql = sql[:-2]
        sql += ');'

        self.cursor.execute(sql, values)
        self.conn.commit()


    def close(self):
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def lastrowid(self):
        return self.cursor.lastrowid



        
