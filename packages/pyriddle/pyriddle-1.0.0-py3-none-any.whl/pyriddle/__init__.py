# src/pyriddle/__init__.py
from .riddle import riddle_factory
from .data import data

get_riddle, get_riddles = riddle_factory(data)
