import mysql.connector as mysql
from model import Access_Model 

class Connection: 

    connection = None
    query = None
    __host_name = str
    __user_name = str
    __password = str
    __database_name = str


    def __init__(host_name, user_name, password, database_name):
        self.__host_name = host_name
        self.__user_name = user_name
        self.__password = password
        self.__database_name = database_name
        # self.__connect()

    def __connect():
        self.connection = mysql.connector.connect(self.__host_name,self.__user_name, self.__password, self.database_name)
        self.query = self.connection.cursor()
                
class Person_DAL(Connection):
    
    pk_person = int
    name_person = int
    fk_access = Access_Model
    
    def __init__(self,host_name, user_name, password, database_name):
        super.__init__(host_name, user_name, password, database_name)

    def insert_person():
        pass
        
    def list_person(pk_person):
        sql = 'SELECT pk_person, name_person,fk_person FROM person  WHERE pk_person  = %s;'

        self.query.execute(sql, (pk_person,))
        result = self.query.fetchone()

        if result:
            self.pk_person = result[0]
            self.name_person = result[1]
            self.fk_access = result[2]
            
        
    def list_all_person():
        pass
        
    def update_person():
        pass
        
    def delete_person():
        pass
        
    