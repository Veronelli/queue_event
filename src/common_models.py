"""
Common project models
"""

from typing import Any
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SingletonMeta(type):
    """
    class Singleton Meta
    """

    _instances: Any = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]