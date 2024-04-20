import random

class Maze:
    def __init__(self, width, height, start=None, end = None, num_rooms = 3, room_size_range = (3, 5)):
        if width % 2 == 0 or height % 2 == 0:
            raise ValueError("Maze dimensions must be odd to ensure proper wall and path placement.")
        self.width = width
        self.height = height
        self.start = start if start else (1, 1)
        self.end = end if end else (height - 2, width - 2)
        self.num_rooms = num_rooms
        self.room_size_range = room_size_range

    def carve_maze(self, start_x, start_y):
        stack = [(start_x, start_y)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while stack:
            x, y = stack.pop()
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1 and self.maze[ny][nx] == 1:
                    self.maze[y + dy][x + dx] = 0
                    self.maze[ny][nx] = 0
                    stack.append((nx, ny))

    def add_rooms(self):
        min_size, max_size = self.room_size_range
        for _ in range(self.num_rooms):
            room_width = random.randint(min_size, max_size)
            room_height = random.randint(min_size, max_size)
            rx = random.randint(1, self.width - room_width - 2)
            ry = random.randint(1, self.height - room_height - 2)

            rx = rx if rx % 2 == 1 else rx + 1
            ry = ry if ry % 2 == 1 else ry + 1

            for i in range(ry, ry + room_height):
                for j in range(rx, rx + room_width):
                    if 1 <= i < self.height - 1 and 1 <= j < self.width - 1:
                        self.maze[i][j] = 0

    def generate(self):
        self.maze = [[1 for _ in range(self.width)] for _ in range(self.height)]
        self.maze[self.start[1]][self.start[0]] = 0
        self.carve_maze(self.start[0], self.start[1])
        if self.num_rooms > 0:
            self.add_rooms()
        self.fill_edges()
        return self

    def fill_edges(self):
        for x in range(self.width):
            self.maze[0][x] = 1
            self.maze[self.height - 1][x] = 1
        for y in range(self.height):
            self.maze[y][0] = 1
            self.maze[y][self.width - 1] = 1

    def solve(self, pathfinder, heuristic):
        if not self.maze:
            self.generate()
        return pathfinder(self.maze, self.start, self.end, heuristic).run()
    
    @property
    def maze(self):
        if not (self.__dict__.get("_maze")):
            self.generate()
        return self._maze
    
    @maze.setter
    def maze(self, value):
        self.__dict__["_maze"] = value

if __name__ == "__main__":
    from algorithms import AStar
    from heuristics import manhattan
    maze = Maze(21, 21, (1, 1))
    print(maze.maze)
    print(maze.solve(AStar, manhattan))

            
    