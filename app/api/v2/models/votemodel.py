from app.db_config import Db

class VoteModel(Db):

    def __init__(self):
     super().__init__()

    def save_vote(self,createdBy,office):
        
        self.cursor.execute(
            "INSERT INTO votes(createdBy,office)VALUES (%s, %s)",
            (createdBy,office))
        self.connect.commit()

    def exist_vote(self,createdBy):
        
        self.cursor.execute(
            "SELECT * from votes WHERE createdBy = {}".format(createdBy))
        vote = self.cursor.fetchall()
        return vote