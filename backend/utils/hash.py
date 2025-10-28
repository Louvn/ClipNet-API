from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(secret):
    return pwd_context.hash(secret)

def verify(secret, hashed):
    return pwd_context.verify(secret, hashed)