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
            logoUrl character varying(150) NOT NULL,
        
            )"""
        queries = [users,offices,parties]
      
        for query in queries:
            if query:
                self.cursor.execute(query)
        self.connect.commit()

    def destroy_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.cursor.execute("DROP TABLE IF EXISTS parties")
        self.cursor.execute("DROP TABLE IF EXISTS offices")
        self.connect.commit()
        self.connect.close()