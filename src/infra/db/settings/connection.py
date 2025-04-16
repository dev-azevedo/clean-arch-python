from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__conneciton_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql",
            "root",
            "root",
            "localhost",
            3306,
            "clean_database",
        )
        self.__engine = self.__create_database__engine()
        
        
    def __create_database__engine(self):
        engine = create_engine(self.__conneciton_string)
        return engine
    
    def get_engine(self):
        return self.__engine