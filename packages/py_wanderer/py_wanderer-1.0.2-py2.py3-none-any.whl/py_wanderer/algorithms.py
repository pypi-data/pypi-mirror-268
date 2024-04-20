import abc
from collections import defaultdict
from heapq import heappop, heappush
from typing import Callable

Heuristic = Callable[[tuple[int, int], tuple[int, int]], float]


class PathfindingAlgorithm(abc.ABC):
    def __init__(
            self,
            grid: list[list[int]],
            start: tuple[int, int], goal: tuple[int, int],
            heuristic_function: Heuristic,
            directions: tuple[tuple[int, int], ...] = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.heuristic_function = heuristic_function
        self.directions = directions
        self.open_set = []
        heappush(self.open_set, (0, start))
        self.came_from = {}
        self.g_score = defaultdict(lambda: float('inf'))
        self.g_score[start] = 0
        self.f_score = defaultdict(lambda: float('inf'))
        self.f_score[start] = self.heuristic_function(start, goal)

    def get_neighbors(self, node):
        directions = self.directions
        neighbors = []
        for dx, dy in directions:
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.grid[nx][ny] == 0:
                neighbors.append((nx, ny))
        return neighbors

    def reconstruct_path(self, current_node):
        path = []
        while current_node in self.came_from:
            next_node = self.came_from[current_node]
            path.append(current_node)
            current_node = next_node
        path.append(self.start)
        return path[::-1]

    @abc.abstractmethod
    def run(self):
        """Run the pathfinding algorithm."""


class Dijkstra(PathfindingAlgorithm):
    def run(self):
        while self.open_set:
            current = heappop(self.open_set)[1]
            if current == self.goal:
                return self.reconstruct_path(current)
            for neighbor in self.get_neighbors(current):
                tentative_g_score = self.g_score[current] + 1
                if tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    self.f_score[neighbor] = self.heuristic_function(neighbor, self.goal)
                    heappush(self.open_set, (self.f_score[neighbor], neighbor))
        return []


class AStar(PathfindingAlgorithm):
    def run(self) -> list[tuple[int, int]]:
        while self.open_set:
            current = heappop(self.open_set)[1]
            if current == self.goal:
                return self.reconstruct_path(current)
            for neighbor in self.get_neighbors(current):
                tentative_g_score = self.g_score[current] + self.heuristic_function(current, neighbor)
                if tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    self.f_score[neighbor] = self.g_score[neighbor] + self.heuristic_function(neighbor, self.goal)
                    heappush(self.open_set, (self.f_score[neighbor], neighbor))
        return []


class ThetaStar(PathfindingAlgorithm):
    # like A* but with line of sight check
    def run(self) -> list[tuple[int, int]]:
        """ Execute the Theta* pathfinding algorithm. """
        while self.open_set:
            current = heappop(self.open_set)[1]
            if current == self.goal:
                return self.reconstruct_path(current)

            for neighbor in self.get_neighbors(current):
                tentative_g_score = self.g_score[current] + self.heuristic_function(current, neighbor)
                if tentative_g_score < self.g_score[neighbor]:
                    if self.has_line_of_sight(current, neighbor):
                        self.came_from[neighbor] = current
                        self.g_score[neighbor] = tentative_g_score
                        estimated_f_score = tentative_g_score + self.heuristic_function(neighbor, self.goal)
                        self.f_score[neighbor] = estimated_f_score
                        heappush(self.open_set, (estimated_f_score, neighbor))

        return []

    def has_line_of_sight(self, a: tuple[int, int], b: tuple[int, int]) -> bool:
        """ Check if there is a direct line of sight between two points in a grid. """
        x0, y0 = a
        x1, y1 = b
        dx = x1 - x0
        dy = y1 - y0
        x_sign = 1 if dx > 0 else -1
        y_sign = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)

        x, y = x0, y0
        if dx > dy:
            p = 2 * dy - dx
            while x != x1:
                x += x_sign
                if p > 0:
                    y += y_sign
                    p -= 2 * dx
                if self.grid[x][y] == 1:
                    return False
                p += 2 * dy
        else:
            p = 2 * dx - dy
            while y != y1:
                y += y_sign
                if p > 0:
                    x += x_sign
                    p -= 2 * dy
                if self.grid[x][y] == 1:
                    return False
                p += 2 * dx

        return True


class JPS(PathfindingAlgorithm):
    def run(self) -> list[tuple[int, int]]:
        """ Execute the Jump Point Search pathfinding algorithm. """
        while self.open_set:
            current = heappop(self.open_set)[1]
            if current == self.goal:
                return self.reconstruct_path(current)

            for neighbor in self.get_neighbors(current):
                tentative_g_score = self.g_score[current] + self.heuristic_function(current, neighbor)
                if tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    estimated_f_score = tentative_g_score + self.heuristic_function(neighbor, self.goal)
                    self.f_score[neighbor] = estimated_f_score
                    heappush(self.open_set, (estimated_f_score, neighbor))

        return []


class IterativeDeepeningDFS(PathfindingAlgorithm):
    def run(self):
        import itertools

        def dls(node, depth):
            if node == self.goal:
                return self.reconstruct_path(node)
            if depth == 0:
                return None
            for neighbor in self.get_neighbors(node):
                if neighbor not in self.came_from:
                    self.came_from[neighbor] = node
                    found = dls(neighbor, depth - 1)
                    if found:
                        return found
            return None

        for depth in itertools.count():
            self.came_from = {self.start: None}
            result = dls(self.start, depth)
            if result is not None:
                return result

        return []


class Swarm(PathfindingAlgorithm):
    def run(self) -> list[tuple[int, int]]:
        open_set_start = []
        open_set_goal = []
        heappush(open_set_start, (0, self.start))
        heappush(open_set_goal, (0, self.goal))

        came_from_start = {self.start: None}
        came_from_goal = {self.goal: None}

        while open_set_start and open_set_goal:
            self.process_set(open_set_start, came_from_start, came_from_goal)
            self.process_set(open_set_goal, came_from_goal, came_from_start)

            if set(came_from_start) & set(came_from_goal):
                meet_node = list(set(came_from_start) & set(came_from_goal))[0]
                return self.reconstruct_bidirectional_path(came_from_start, came_from_goal, meet_node, meet_node)
        return []

    def process_set(self, open_set, came_from, other_came_from):
        if open_set:
            current = heappop(open_set)[1]
            for neighbor in self.get_neighbors(current):
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    if neighbor in other_came_from:
                        return
                    heappush(open_set, (self.heuristic_function(neighbor, self.goal), neighbor))

    def reconstruct_bidirectional_path(self, came_from_start, came_from_goal, meet_start, meet_goal):
        # reconstruct path from both sides meeting at a common node
        path_start = []
        while meet_start:
            path_start.append(meet_start)
            meet_start = came_from_start[meet_start]
        path_goal = []
        while meet_goal:
            path_goal.append(meet_goal)
            meet_goal = came_from_goal[meet_goal]
        path_start.reverse()
        return path_start + path_goal[1:]


class DepthFirstSearch(PathfindingAlgorithm):
    def run(self) -> list[tuple[int, int]]:
        stack = [self.start]
        self.came_from[self.start] = None

        while stack:
            current = stack.pop()
            if current == self.goal:
                return self.reconstruct_path(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in self.came_from:
                    self.came_from[neighbor] = current
                    stack.append(neighbor)
        return []


class BellmanFord(PathfindingAlgorithm):
    def run(self) -> list[tuple[int, int]]:
        self.g_score[self.start] = 0

        for _ in range(len(self.grid) * len(self.grid[0]) - 1):
            made_changes = False
            for u in range(len(self.grid)):
                for v in range(len(self.grid[0])):
                    current = (u, v)
                    if self.g_score[current] != float('inf'):
                        for neighbor in self.get_neighbors(current):
                            weight = 1  # Assume all edges have weight 1
                            if self.g_score[current] + weight < self.g_score[neighbor]:
                                self.g_score[neighbor] = self.g_score[current] + weight
                                self.came_from[neighbor] = current
                                made_changes = True
            if not made_changes:
                break

        if self.g_score[self.goal] != float('inf'):
            return self.reconstruct_path(self.goal)
        return []


ALGORITHMS = [Dijkstra, AStar, ThetaStar, JPS, IterativeDeepeningDFS, Swarm, DepthFirstSearch, BellmanFord]
