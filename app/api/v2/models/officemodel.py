from app.db_config import Db

class OfficeModel(Db):
    '''This class has queries that access and manipulate data in  table offices in database'''

    def __init__(self):
     super().__init__()

    def save_office(self,name,age,office_type,education):
        
        self.cursor.execute(
            "INSERT INTO offices(name,age,office_type,education)VALUES (%s, %s, %s, %s)",
            (name,age,office_type,education))
        self.connect.commit()
  
    def find_by_name(self,name):  
        '''solves the problem of duplication of offices'''
           
        self.cursor.execute("SELECT * from offices WHERE name = '{}'".format(name))
        office = self.cursor.fetchall()
        return office
  
    def get_all(self):
        self.cursor.execute("SELECT * from offices")
        office_list = self.cursor.fetchall()
        return office_list
  
    def find_by_id(self,office_id):     
        self.cursor.execute("SELECT * from offices WHERE office_id = {}".format(office_id))
        party= self.cursor.fetchall()
        return party
    
    def delete_by_id(self,office_id): 
        self.cursor.find_by_id(office_id)    
        self.cursor.execute("DELETE * from offices WHERE office_id = {}".format(office_id))
        self.connect.commit()
    

    def valid(self,data):
        if data.isalnum():
            return True
        return False
    
    def valid_type(self,data):
        if data.isspace() or data == "":
           return False
    
    def valid_digits(self,data):
        if data.isdigit():
            return True
        return False
        
    def length_long(self,data):
        if len(data) < 5:
            return False
    def length_short(self,data):
        if len(data) > 4:
            return False
    def valid_office_type(self,data,office_type):
        if office_type == data['state'] or office_type == data['federal'] or office_type == data['legislature'] or office_type== data['state'] :
            return True
        return False  