from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"

        results = connectToMySQL(cls.DB).query_db(query)
        
        new_list = []
        
        for row in results:
            new_list.append(cls(row))
        return new_list
    
    @classmethod
    def get_dojo_by_id(cls, id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {
            'id':id
        }
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(f"dojo by id: {results[0]}")
        return results[0]

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        new_dojo = connectToMySQL(cls.DB).query_db(query, data)
        return new_dojo