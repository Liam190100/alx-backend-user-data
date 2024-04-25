import bcrypt
from sqlalchemy.exc import NoResultFound

from db import DB
from user import User

"""module of authentication.
"""

def _hash_password(password: str) -> bytes:
    """Hashes a password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class authentication database.
    """

    def __init__(self):
        """Initializes new Auth instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Adds a new user db.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """user login details are valid.
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            return False
        return False
