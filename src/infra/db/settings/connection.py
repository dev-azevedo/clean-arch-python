from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
        self.session = None
        
        
    def __create_database__engine(self):
        engine = create_engine(self.__conneciton_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()