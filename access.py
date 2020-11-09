import status
import os
import pymysql
import validation
import utilities

class Access_Db():

    def __init__(self):
        print("Creation")
        status_type   = "latest"
        self.conn = None
        try:
            self.rds_host = os.environ['RDS']
            self.name = os.environ['NAME']
            self.password = os.environ['PASSWORD']
            self.db_name = os.environ['DB']
            self.port = os.environ['PORT_NUMBER']
        except:
            print("Environment variables not set")

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
        
    def createUser(self, new_user):
        print("Creating record in db")
        if new_user == None:
            return status.failure_db()

        #new_user = validation.newUser(user)
        #if new_user.error == True:
        #    return status.failure_parameters()
        
        try:
            print("Accessing db")
            self.open_connection()
            if self.conn is None:
                print("Db is none")
                return status.failure_db()
            cursor = self.conn.cursor()
            # Create a new record
            

            sql = "INSERT INTO `users` (`id`, `email`, `username`, `dob`, `firstName`, `lastName`, `createdDate`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            insert_tuple = (new_user.userId, new_user.email, new_user.username, 
            "test-dob", "first", "last", utilities.getTime())
            cursor.execute(sql, insert_tuple)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

            cursor.close()

        except pymysql.MySQLError as e:
            print("Error: ",e)
        else:
            self.conn.close()

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
                if row is not None:
                    string = validation.convertUser(row)
                    return status.return_user(string)
                return status.success()
                
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

    