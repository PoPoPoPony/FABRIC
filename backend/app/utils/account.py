import random
import string
from passlib.hash import sha512_crypt



def encrypt(frontend_hashed_pwd):
    salt = generate_random_string()
    backend_hashed_pwd = sha512_crypt.hash(frontend_hashed_pwd, salt=salt)

    return backend_hashed_pwd, salt


def generate_random_string():
    # passlib sha512_crypt 的salt只允許0-16
    min_length = 1
    max_length = 16
    random_length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(random_length))

    return random_string

def verify_account(backend_hashed_pwd, frontend_hashed_pwd, salt):
    backend_hashed_pwd = f"$6$rounds=656000${salt}${backend_hashed_pwd}"
    result = sha512_crypt.verify(frontend_hashed_pwd, backend_hashed_pwd)

    return result