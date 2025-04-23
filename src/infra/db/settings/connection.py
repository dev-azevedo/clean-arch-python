from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

USER_DB = config("USER_DB")
PASS_DB = config("PASS_DB")
HOST_DB = config("HOST_DB")
PORT_DB = config("PORT_DB")
NAME_DB = config("NAME_DB")


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__conneciton_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql",
            USER_DB,
            PASS_DB,
            HOST_DB,
            PORT_DB,
            NAME_DB,
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