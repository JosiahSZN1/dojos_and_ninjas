from flask_app.config.mysqlconnection import connectToMySQL
mydb = 'dojos_and_ninjas_schema'
# route.py
class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_dojo(cls, data):
        query = '''
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        '''
        connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def get_all_dojos(cls):
        query = '''
        SELECT *
        FROM dojos
        '''
        return connectToMySQL(mydb).query_db(query)
    
    @classmethod
    def get_one_dojo(cls,data):
        query = '''
        SELECT *
        FROM dojos
        WHERE id = %(id)s;
        '''
        return connectToMySQL(mydb).query_db(query,data)[0]