from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        
        results = connectToMySQL(cls.DB).query_db(query)
        
        new_list = []
        
        for row in results:
            new_list.append(cls(row))
        return new_list
    
    @classmethod
    def get_one_dojo_with_ninjas(cls, dojo_id):
        data = {'dojo_id':dojo_id}
        query = "Select * from ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(f"results: {results}")
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        print(f"Ninjas in this dojo: {ninjas}")
        return ninjas
    
    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES(%(fname)s, %(lname)s, %(age)s, %(dojo_id)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(f"results: {results}")
        return data['dojo_id']