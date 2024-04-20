"""Maze builder and pathfinding algorithms."""

from .algorithms import ALGORITHMS, PathfindingAlgorithm, Heuristic
from .heuristics import HEURISTICS
from .maze import Maze

__version__ = "1.0.3"

ALGORITHMS = ALGORITHMS
HEURISTICS = HEURISTICS


def __getattr__(name):
    if name in globals():
        return globals()[name]

    if name[0].isupper():
        return next(algorithm for algorithm in ALGORITHMS if algorithm.__name__ == name)
    else:
        return next(heuristic for heuristic in HEURISTICS if heuristic.__name__ == name)
