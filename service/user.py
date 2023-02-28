import base64
import hashlib

from constans import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO
class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        movies = self.dao.get_all()
        return movies

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao, 201

    def delete(self, rid):
        self.dao.delete(rid), 204

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)
    
    def get_by_username(self, username):
        return self.dao.get_by_username(username)


