from repo.user import UserRepo
from schemas.user import User, UserUpdate
from fastapi import HTTPException


class UserService():
    def __init__(self, db) -> None:
        self.repo = UserRepo(db=db)
    
    def create_new(self, user_create: User) -> User:
        existing_user = self.repo.get_by_email(user_create.email)
        if existing_user:
            raise HTTPException(status_code=409, detail="User with this email already exists")

        new_user = self.repo.create(user_create)
        return User.from_orm(new_user)

    
    def get_user_for_auth(self, username: str, password: str) -> User:
        user = self.repo.get_by_username(username, password)

        if user is None:
            raise  HTTPException(status_code=403)
        return User.from_orm(user)
    
    def get_by_username(self, username: str) -> User:
        user = self.repo.get_by_username(username)
        if user is None:
            raise  HTTPException(status_code=403)
        return User.from_orm(user)
    

    def update_avatar(self, username: str, avatar_public_id: str):
        user = self.repo.get_by_username(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.avatar_public_id = avatar_public_id
        self.repo.commit()
        return user
    


    
   
