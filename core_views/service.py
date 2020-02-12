from common_utils import MySqlCoordinator


class Authorization:

    def __init__(self):
        self.mysql = MySqlCoordinator()

    def get_authorization_token(self, data):
        query = 'select * from mentor_user where username = "{}" and password = "{}"'.format(data.get("username"), data.get("password"))
        return self.mysql.query_db(query)

    def get_question(self, data):
        query = 'select * from ms_user where username = "{}" and password = "{}"'.format(data.get("username"), data.get("password"))
        result = self.mysql.query_db_one(query)
        sql = "select * from test_question_master where test_question_id = {}".format(result.get("fellowshipplan_id"))
        result = self.mysql.query_db_one(sql)
        result = {"repository_name": result.get("repository_name")}
        return result 

    def update_repository_status(self, data):        
        query = "insert into repository_status(username, repository_name) values({}, {})".format(data.get("username"), data.get("repository_name"))
        result = self.mysql.write_db(query)
        return dict()
    
    def get_all_questions(self):
        query = "select * from test_question_master"
        result = self.mysql.query_db(query)        
        return {"question_list": result}

    def get_commands(self, data):
        query = 'select * from test_question_master where test_question_id = "{}"'.format(data.get("repository_id"))
        result = self.mysql.query_db_one(query)
        command_string1 = "bridgel --get_question {}".format(result.get("repository_name"))
        command_string2 = "bridgel --enter_solution {}".format(result.get("repository_name"))
        return {"command_string1": command_string1, "command_string2": command_string2 }

    def add_final_tags(self, data):
        tag = "https://github.com/aashishogale/{}_{}/tree/v-1.0".format(data.get("username"), data.get("repository_name"))
        query = 'select * from ms_user where username = "{}"'.format(data.get("username"))
        result = self.mysql.query_db_one(query)
        save_query = "insert into tag_path_table (username, mentor_name, tag_link) values({}, {}, {})".format(data.get("username"), result.get("mentor_name"), tag)
        result = self.mysql.write_db(save_query)
        return dict()
    
    def getMentortags(self):
        query =  "select * from tag_path_table"
        result = self.mysql.query_db(query)
        return {"git_list": result}
