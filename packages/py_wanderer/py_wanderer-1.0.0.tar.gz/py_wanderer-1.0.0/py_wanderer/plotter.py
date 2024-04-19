try:
    import matplotlib.pyplot as plt
except ImportError:
    print("You need to install matplotlib to use this module.")
    exit(1)
    
from .maze import Maze

def plot(maze: Maze, path: list[tuple[int, int]]):
    """Plot the maze and the path."""
    fig, ax = plt.subplots()
    ax.imshow(maze.maze, cmap="binary")
    if path:
        ax.plot([y for x, y in path], [x for x, y in path], "b-")
    ax.plot(maze.start[0], maze.start[1], "go")
    ax.plot(maze.end[0], maze.end[1], "ro")
    plt.show()
