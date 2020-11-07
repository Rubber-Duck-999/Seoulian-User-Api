import json
import logging
import uuid
import status
import os
import pymysql
import hashlib
import validation
import utilities

class Access_Db():

    def __init__(self):
        print("Creation")
        status_type   = "latest"
        self.conn = None
        try:
            self.rds_host = os.environ['RDS']
            print(self.rds_host)
            self.name = os.environ['NAME']
            self.password = os.environ['PASSWORD']
            self.db_name = os.environ['DB']
            self.port = os.environ['PORT_NUMBER']
        except:
            print("Environment variables not set")

    def generateID(self):
        print("Generating id")
        random_data = os.urandom(128)
        id = hashlib.md5(random_data).hexdigest()[:32]
        return id


    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                print("Connecting to db")
                self.conn = pymysql.connect(
                    host=self.rds_host,
                    user=self.name,
                    passwd=self.password,
                    port=int(self.port),
                    db=self.db_name,
                    connect_timeout=5
                )
        except pymysql.MySQLError as e:
            print("Error: ", e)
        
    def createUser(self, user):
        print("Creating record in db")
        if user == None:
            return status.failure_db()

        new_user = validation.newUser(user)
        if new_user.error == True:
            return status.failure_parameters()
        
        try:
            print("Accessing db")
            self.open_connection()
            if self.conn is None:
                print("Db is none")
                return status.failure_db()
            cursor = self.conn.cursor()
            # Create a new record
            

            sql = "INSERT INTO `users` (`id`, `email`, `username`, `dob`, "
            "`firstName`, `lastName`, `createdDate`) "
            "VALUES (%s, %s, %s, %s, %s, %s, '%s')"
            insert_tuple = (self.generateID(), new_user['email'], new_user['username'], 
            new_user['dob'], new_user['firstName'], new_user['lastName'], utilities.getTime())
            cursor.execute(sql, insert_tuple)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

            cursor.close()

        except pymysql.MySQLError as e:
            print("Error: ",e)
        else:
            self.conn.close()
            return status.success()

    def getUserPreferences(self, user_request):
        print("Creating query for getting status record")
        if user_request is None:
            return status.failure_parameters()

        try:
            print("Accessing db")
            self.open_connection()
            if self.conn is None:
                print("Db is none")
                return status.failure_db()
            cursor = self.conn.cursor()
            # Create a new record

            if user_request["username"] is not None:
                cursor.execute("SELECT * FROM users WHERE username=%s", user_request['username'])
                row = cursor.fetchone()
                print(row)
            else:
                return status.failure_parameters()

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()
            cursor.close()
            return status.success()

        except pymysql.MySQLError as e:
            print("Error: ",e)
        else:
            self.conn.close()
            return status.success()

    