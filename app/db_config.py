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
        query = [users]
        self.cursor.execute(query)
        self.connect.commit()
        self.connect.close()