from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data): # data is a dictionary representing a record (row) from the database
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        # self.created_at = data["NOW"]
        self.users = []

# queries go in here
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL("users_schema").query_db(query, data)


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        user_instances = []
        if len(results) == 0:
            return []
        else:
            for user_dictionary in results:
                user_instances.append(cls(user_dictionary))
            return user_instances
