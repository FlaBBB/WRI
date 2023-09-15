import sqlite3

db_list = ["my-database-1.db", "my-database-2.db"]

class connect:
    _instance = None
    __db_list = dict()
    
    def __new__(cls, database_name):
        if cls._instance == None:
            cls._instance = super(connect, cls).__new__(cls)

        if database_name not in cls.__db_list:
            cls.__db_list[database_name] = sqlite3.connect(database_name)

        return cls._instance
    
    def __init__(self, database_name) -> None:
        self.database_name = database_name
    
    def connect(self) -> sqlite3.Connection:
        return self.__db_list[self.database_name]
    
    def get_db_list(self) -> dict:
        return self.__db_list

class test:
    connection = connect(db_list[0]).connect()

if __name__ == "__main__":
    db_list = ["my-database-1.db", "my-database-2.db"]
    # for _ in range(10):
    #     connection = connect(random.choice(db_list))
    #     print(sqlite3.connect(random.choice(db_list)))
        
    print(connect(db_list[0]))
    print(connect(db_list[1]))
    print(connect(db_list[0]).get_db_list())
    print(connect(db_list[1]).get_db_list())
    obj_test = test()
    print(connect(db_list[0]).connect())
    print(obj_test.connection)