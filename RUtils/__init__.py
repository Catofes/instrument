import random
import string
from singleton import Singleton
from database import RDateBasePool
from config import RConfig
from error import RError
from session import RMemorySessionStore


def generate_code(length=64):
    if length < 1:
        return False
    return ''.join(random.sample(string.ascii_letters + string.digits, length))
