import psycopg2
from flask import current_app
from psycopg2.extras import RealDictCursor


class Db:
    def __init__(self):

        self.database_url = current_app.config['DATABASE_URL']
        self.connect = psycopg2.connect(self.database_url)
        self.cursor = self.connect.cursor(cursor_factory=RealDictCursor)

    def init_app(self, app):
        self.connect = psycopg2.connect(app.config['DATABASE_URL'])
        self.cursor = self.connect.cursor(cursor_factory=RealDictCursor)

    def create_tables(self):
        users = """CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY NOT NULL,
            first_name character varying(100) NOT NULL,
            last_name character varying(100) NOT NULL,
            username character varying(100) NOT NULL,
            email character varying(100) NOT NULL,
            phonenumber character varying(10) NOT NULL,
            password character varying(150) NOT NULL,
            is_admin BOOLEAN DEFAULT FALSE
            )"""
        
        offices = """CREATE TABLE IF NOT EXISTS offices(
            office_id serial PRIMARY KEY NOT NULL,
            name character varying(100) NOT NULL,
            age character varying(100) NOT NULL,
            Office_type character varying(100) NOT NULL,
            education character varying(100) NOT NULL
            )"""
        
        parties = """CREATE TABLE IF NOT EXISTS parties(
            party_id serial PRIMARY KEY NOT NULL,
            first_name character varying(100) NOT NULL,
            abbreviations character varying(100) NOT NULL,
            chairperson character varying(100) NOT NULL,
            members character varying(100) NOT NULL,
            address character varying(10) NOT NULL,
            logoUrl character varying(150) NOT NULL
        
            )"""

        candidates = """CREATE TABLE IF NOT EXISTS candidates(
            id serial NOT NULL,
            office int NOT NULL references offices(office_id) on delete cascade,
            party int NOT NULL references parties(party_id) on delete cascade,
            candidate int NOT NULL references users(user_id) on delete cascade,
            PRIMARY KEY(office,candidate)
         )"""
 
        votes = """CREATE TABLE IF NOT EXISTS votes(
            id serial NOT NULL,
            createdOn TIMESTAMP DEFAULT now(),
            createdBy int NOT NULL references users(user_id) on delete cascade,
            candidate int NOT NULL references users(user_id) on delete cascade,
            office int NOT NULL references  offices(office_id) on delete cascade,
            PRIMARY KEY(createdBy,office)
         )"""
        

         
        queries = [users,offices,parties,candidates,votes]
      
        for query in queries:
            if query:
                self.cursor.execute(query)
        self.connect.commit()

    def destroy_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS votes")
        self.cursor.execute("DROP TABLE IF EXISTS candidates")
        self.cursor.execute("DROP TABLE IF EXISTS parties")
        self.cursor.execute("DROP TABLE IF EXISTS offices")
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.connect.commit()
        self.connect.close()