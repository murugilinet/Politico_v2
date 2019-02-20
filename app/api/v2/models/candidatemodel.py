from app.db_config import Db

class CandidateModel(Db):
    '''This class has queries that access and manipulate data in  table candidates in database'''

    def __init__(self):
     super().__init__()

    def save_candidate(self,office,party,candidate):
        
        self.cursor.execute(
            "INSERT INTO candidates(office,party,candidate)VALUES (%s, %s, %s)",
            (office,party,candidate))
        self.connect.commit()
    
    def exist_candidate(self,candidate):
        
        self.cursor.execute(
            "SELECT * from candidates WHERE candidate ={}".format(candidate))
        politician = self.cursor.fetchall()
        return politician

  