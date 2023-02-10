from flask_app.config.mysqlconnection import connectToMySQL
mydb = 'dojos_and_ninjas_schema'
# ninja.py
class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def add_ninja(cls, data):
        query = '''
        INSERT INTO ninjas (dojo_id, first_name, last_name, age)
        VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s)
        '''
        connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def get_all_ninjas(cls, data):
        query = '''
        SELECT *
        FROM ninjas
        JOIN dojos ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s
        '''
        return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def delete_ninja(cls,data):
        query = '''
        DELETE *
        FROM ninjas
        WHERE id = %(id)s;
        '''
        connectToMySQL(mydb).query_db(query, data)