from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler
from src.data.interfaces.users_repository import UsersRepository as IUsersRepository
from src.domain.models.users import Users

class UsersRepository(IUsersRepository):
    
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try: 
                new_registry = UsersEntity(first_name=first_name, last_name=last_name, age=age)
                database.session.add(new_registry)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    @classmethod
    def select_user(cls, first_name: str) -> list[Users]:
        with DBConnectionHandler() as database:
            try: 
                users = (
                    database.session.query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all()
                )
                
                return users
            except Exception as e:
                database.session.rollback()
                raise e