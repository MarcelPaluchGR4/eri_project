import heapq

from customtkinter import CTkButton

PASSABLE_COLOR = "blue"
BLOCKED_COLOR = "red"
VISITED_COLOR = "gray"
PATH_COLOR = "purple"


class Astar:
    open_set = []
    closed_set = []

    def __init__(self, grid: list[list[CTkButton]]) -> None:
        open_list = []
        closed_list = set()
        came_from = {}
        self.start = (0, 19)
        self.end = (19, 0)
        self.rows = 20
        self.cols = 20
        self.grid = grid

        g_costs = {self.start: 0}
        f_costs = {self.start: self.heuristic(self.start, self.end)}

        heapq.heappush(open_list, (f_costs[self.start], self.start))

        while open_list:
            _, current = heapq.heappop(open_list)

            if current == self.end:
                self.reconstruct_path(came_from)
                return

            closed_list.add(current)

            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                if (
                    neighbor in closed_list
                    or self.grid[neighbor[0]][neighbor[1]].cget("fg_color")
                    == BLOCKED_COLOR
                ):
                    continue

                tentative_g_cost = g_costs[current] + 1
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    came_from[neighbor] = current
                    g_costs[neighbor] = tentative_g_cost
                    f_costs[neighbor] = tentative_g_cost + self.heuristic(
                        neighbor, self.end
                    )

                    if neighbor not in [x[1] for x in open_list]:
                        heapq.heappush(open_list, (f_costs[neighbor], neighbor))

            self.update_grid_visited()

    def reconstruct_path(self, came_from):
        current = self.end
        while current != self.start:
            self.grid[current[0]][current[1]].configure(fg_color=PATH_COLOR)
            current = came_from[current]

    def heuristic(self, a, b):
        return abs(a[0] - a[1]) + abs(b[0] - b[1])

    def get_neighbors(self, current):
        row, col = current
        neighbors = []
        if col < self.cols - 1:
            neighbors.append((row, col + 1))  # Right
        if row > 0:
            neighbors.append((row - 1, col))  # Up
        if row < self.rows - 1:
            neighbors.append((row + 1, col))  # Down
        if col > 0:
            neighbors.append((row, col - 1))  # Left

        return neighbors

    def update_grid_visited(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j].cget("fg_color") == VISITED_COLOR:
                    self.grid[i][j].configure(fg_color=VISITED_COLOR)
