from app.db_config import Db

class PartyModel(Db):
    '''This class has queries that access and manipulate data in party table in database'''

    def __init__(self):
     super().__init__()

    def save_party(self,name,abbreviations,chairperson,members,address,logoUrl):
        
        self.cursor.execute(
            "INSERT INTO parties(first_name,abbreviations,chairperson,members,address,logoUrl)VALUES (%s,%s,%s,%s,%s,%s)",
            (name,abbreviations,chairperson,members,address,logoUrl))
        self.connect.commit()
  
    def get_all(self):
        self.cursor.execute("SELECT * from parties")
        party_list = self.cursor.fetchall()
        return party_list
  
    def find_by_id(self,party_id):     
        self.cursor.execute("SELECT * from parties WHERE party_id = {}".format(party_id))
        party= self.cursor.fetchall()
        return party
    
    def find_by_name(self,name):  
        '''solves the problem of duplication of parties'''
           
        self.cursor.execute("SELECT * from parties WHERE name '{}'".format(name))
        party= self.cursor.fetchall()
        if party:
            return False
    
    def delete_by_id(self,party_id): 
        self.cursor.find_by_id(party_id)    
        self.cursor.execute("DELETE * from parties WHERE party_id {}".format(party_id))
        self.connect.commit()
    
    def updatename(self,party_id,name):   
        self.cursor.execute("UPDATE * parties SET name = '{}' WHERE party_id {}".format(name,party_id))
        self.connect.commit()

    def valid(self,data):
        if data.isalnum:
            return True
        return False
    
    def valid_type(self,data):
        if data.isalpha():
            return True
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
    