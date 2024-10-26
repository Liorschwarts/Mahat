from typing import Any, List, Tuple
from dal import get_mysql_session
from sqlalchemy import select
from modals import User, UserCreate, UserUpdate, UserResponse
from security import get_password_hash

class UsersBL:
    def __init__(self) -> None:
        self._mysql_session = get_mysql_session()
    
    def __del__(self) -> None:
        self._mysql_session.close()
        
    def create_user(self, user_create: UserCreate) -> UserResponse:
        user = user_create.model_dump()
        user['hashed_password'] = get_password_hash(user_create.password)
        
        user = User(**user)
        self._mysql_session.add(user)
        self._mysql_session.commit()
        self._mysql_session.refresh(user)
        
        return UserResponse.model_validate(user)

    def get_users(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        users: List[Tuple[User, Any]] = self._mysql_session.exec(select(User).offset(skip).limit(limit)).all()
        return [UserResponse.model_validate(user[0]) for user in users]
    
    def get_user(self, id: int) -> UserResponse:
        user: User = self._mysql_session.exec(select(User).filter(User.id == id)).first()[0]
        
        if not user:
            raise ValueError(f"User with id {id} not found")
        
        return UserResponse.model_validate(user)
    
    def update_user(self, user_id: int, user_update: UserUpdate) -> UserResponse:
        statement = select(User).where(User.id == user_id)
        user = self._mysql_session.exec(statement).first()[0]
        
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        
        update_data = user_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
        
        self._mysql_session.commit()
        self._mysql_session.refresh(user)
        
        return UserResponse.model_validate(user)
    
    def delete_user(self, user_id: int) -> UserResponse:
        statement = select(User).where(User.id == user_id)
        user = self._mysql_session.exec(statement).first()[0]
        
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        
        self._mysql_session.delete(user)
        self._mysql_session.commit()
        
        return UserResponse.model_validate(user)