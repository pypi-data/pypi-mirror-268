import json
import pymysql

class kardb:
    def __init__(self, dbname, host="", user="", passwd=""):
        self.dbname = dbname
        self.docname = 'main'
        self.host = host
        self.user = user
        self.passwd = passwd

        try:
            self.connect()
        except pymysql.err.OperationalError:
            self.create_database()
            self.connect()

        self.data = {}
        self.loaddoc()

    def create_database(self):
        self.db = pymysql.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd
        )
        self.mycursor = self.db.cursor()

        query = f'create database if not exists {self.dbname}'
        self.mycursor.execute(query)

        query = f'use {self.dbname}'
        self.mycursor.execute(query)

        self.createdoc('main')
        self.db.commit()

        self.loaddoc()

        self.mycursor.close()
        self.db.close()

    def connect(self):
        self.db = pymysql.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            database = self.dbname
            )

        self.mycursor = self.db.cursor()

        query = f"use {self.dbname}"
        self.mycursor.execute(query)


    def disconnect(self):
        self.mycursor.close()
        self.db.close()

    def createdoc(self, docname):
        self.docname = docname

        query = f"""create table if not exists {docname} (
        data JSON)
        """
        self.mycursor.execute(query)

        query = f"insert into {docname} values('{dict()}')"
        self.mycursor.execute(query)

    def loaddoc(self):
        query = f"""select * from {self.docname}"""
        self.mycursor.execute(query)

        data = self.mycursor.fetchall()[0]
        if data == tuple():
            data = {}
        else:
            data = json.loads(data[0])
            
        self.data.clear()
        self.data.update(data)

    def changedoc(self,docname):
        self.save()
        self.docname = docname

        self.loaddoc()

    def renamedoc(self, old_docname, new_docname):
        query = f"""rename table {old_docname} to {new_docname}"""
        self.mycursor.execute(query)

    def deletedoc(self, docname):
        if docname == self.docname:
            self.docname = "main"
            self.loaddoc()

        query = f"""drop table {docname}"""
        self.mycursor.execute(query)

    def cacdoc(self, docname):
        self.createdoc(docname)
        self.changedoc(docname)

    def savedoc(self):
        json_data = json.dumps(self.data)

        query = f"""update {self.docname}
        set data = '{json_data}'"""
        self.mycursor.execute(query)

        self.db.commit()

    def updatedoc(self,branch = None):
        if not (branch == None) :
            changeddata = branch

        else:
            changeddata = self.data.copy()

        streamdata = self.loaddoc()
        if streamdata == None:
            streamdata = {}

        streamdata.update(changeddata)
        streamdata = json.dumps(streamdata)

        query = f"""update {self.docname}
        set data = '{streamdata}'"""
        self.mycursor.execute(query)

        self.db.commit()

    def commit(self):
        self.db.commit()