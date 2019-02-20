from app.db_config import Db

class VoteModel(Db):

    def __init__(self):
     super().__init__()

    def save_vote(self,createdBy,candidate,office):
        
        self.cursor.execute(
            "INSERT INTO votes(createdBy,candidate,office)VALUES (%s, %s,%s)",
            (createdBy,candidate,office))
        self.connect.commit()

    def exist_vote(self,createdBy):
        
        self.cursor.execute(
            "SELECT * from votes WHERE createdBy = {}".format(createdBy))
        vote = self.cursor.fetchall()
        return vote
    
    def get_all(self):
        self.cursor.execute("SELECT * from votes")
        total_votes = self.cursor.fetchall()
        return total_votes
   
    def get_results(self,office_id):
        self.cursor.execute(
            """
            SELECT concat_ws(' ',users.first_name,users.last_name) AS candidate,
            offices.name as office,
            (SELECT COUNT(*)
              FROM  votes As p
              WHERE p.candidate = e.candidate
              GROUP BY p.candidate
            ) AS results
            FROM votes AS e
            INNER JOIN users on users.user_id = e.candidate
            INNER JOIN offices ON offices.office_id = e.office
            WHERE office = {}
            GROUP BY e.candidate,users.first_name,users.last_name,offices.name
            """.format(office_id))
        results = self.cursor.fetchall()
        return results
    