import os
import hashlib
from models.users import UsertDB


class UserRepo():
    def __init__(self, db) -> None:
        self.db = db


    def create(self, user):
        password, salt = self.hash_password(user.password)
        new_user = UsertDB(**user.dict())
        new_user.password = password
        new_user.salt = salt
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def get_by_username(self, username):
        return self.db.query(UsertDB).filter(UsertDB.username == username).first()
    
    def get_by_email(self, email):
        return self.db.query(UsertDB).filter(UsertDB.email == email).first()
        

    def get_user_check_pass(self, username, password):
        user = self.db.query(UsertDB).filter(UsertDB.username == username).first()
        password_from_db = user.password
        user_salt = user.salt
        hashed_pass, _ = self.hash_password(password=password, salt=user_salt)
        if hashed_pass==password_from_db:
            return user
        else:
            return None
    

    def generate_salt(self):
        return os.urandom(16)  
    
    def hash_password(self, password, salt=None):
        if salt is None:
            salt = self.generate_salt()
        else:
            salt = bytes.fromhex(salt)  
        salted_password = password.encode() + salt
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return str(hashed_password), str(salt.hex())
    
    def verify_password(self, plain_password, hashed_password, salt):
        return hashed_password == self.hash_password(plain_password, salt)[0]
     