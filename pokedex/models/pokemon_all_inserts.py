#Continuing from startup_inserts.py work...

from sqlmodel import Session
from models import Pokemon
from dependencies import get_engine #will be refactored