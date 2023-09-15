import json
from time import sleep
from random import uniform

class caching:
    __cached = list()

    def get_cached(self, queries):
        pass

    def set_cached(self, queries, data):
        pass

class connection:
    cache = caching()
    
    def __init__(self, database_name:str) -> None:
        self.database = open(f"{database_name}.json", "rw")
        self.parsed_database = json.loads(self.database.read())
        self.columns = list(self.parsed_database[0].keys())
            
        sleep(uniform(0.5, 2)) # anggap saja ada delay detik untuk koneksi
    
    def get(self, get_data):
        for g in get_data:
            if g not in self.columns:
                raise "column not found"
            

class connection_helper:
    __instance = dict()
    
    def __init__(self, database_name) -> connection:
        if database_name not in self.__instance:
            self.__instance[database_name] = connection(database_name)
        return self.__instance[database_name]