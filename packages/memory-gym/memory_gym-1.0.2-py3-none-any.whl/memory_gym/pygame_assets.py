import math
import numpy as np
import pygame

from pygame.math import Vector2

class GridPositionSampler():
    def __init__(self, world_dim) -> None:
        """Initialize the GridPositionSampler with the grid dimension.

        Arguments:
            world_dim {int} -- The dimension of the grid
        """
        self.grid_dim = world_dim
        self.area = np.arange(0, self.grid_dim ** 2, dtype=np.int32).reshape((self.grid_dim, self.grid_dim))

    def reset(self, rng):
        """Reset the grid position sampler with a new random number generator and an empty spawn mask.

        Arguments:
            rng {numpy.random.Generator} -- A random number generator instance.
        """
        self.spawn_mask = np.zeros((self.grid_dim, self.grid_dim), dtype=np.bool_)
        self.rng = rng

    def sample(self, block_radius = 21):
        """Sample a random non-overlapping position on the grid.

        Arguments:
            block_radius {int} -- The block radius to avoid overlapping positions (default: 21).

        Returns:
            {tuple} -- A tuple containing the x and y coordinates of the sampled position.
        """
        # Retrieve valid indices
        spawn_area = np.ma.array(self.area, mask=self.spawn_mask).compressed()
        # Sample index
        cell_id = self.rng.integers(0, len(spawn_area))
        # Convert to 2D indices
        y = int(spawn_area[cell_id] / self.grid_dim)
        x = int(spawn_area[cell_id] % self.grid_dim)
        # Update spawn mask
        self.block_spawn_position((x, y), block_radius)
        return (x, y)

    def block_spawn_position(self, pos, block_radius = 21):
        """Block the grid positions around the given position by updating the spawn mask to avoid overlapping.

        Arguments:
            pos {tuple} -- A tuple containing the x and y coordinates of the position.
            block_radius {int} -- The block radius to avoid overlapping positions (default: 21).
        """
        x = pos[0]
        y = pos[1]
        n = self.grid_dim
        r = block_radius
        y, x = np.ogrid[-y:n-y, -x:n-x]
        mask = x*x + y*y < r*r
        self.spawn_mask[mask] = True

class Spotlight():
    def __init__(self, dim, radius, speed, rng, has_border = False) -> None:
        """Initialize the Spotlight with the specified parameters.

        Arguments:
            dim {int} -- The dimension of the square screen (assuming width and height are the same).
            radius {float} -- The radius of the spotlight circle.
            speed {float} -- The speed of the spotlight movement (between 0 and 1).
            rng {numpy.random.Generator} -- A random number generator instance.
            has_border {bool} -- Whether to display a border around the spotlight (default: False).
        """
        self.speed = speed
        self.t = 0
        self.done = False
        self.has_border = has_border
        # Center of the screen
        center = (dim // 2, dim // 2)
        # Length of the diagonal of the screen
        diagonal = math.sqrt(math.pow(dim, 2) + math.pow(dim, 2))
        # Determine final spawn radius to ensure that spotlights are not visible upon spawning
        self.spawn_radius = diagonal / 2 + radius
        self.radius = radius

        # Sample angles for start, end and offset position
        start_angle = rng.integers(0, 360)
        inverted_angle = start_angle + 180
        target_angle = inverted_angle + rng.integers(-45, 45)
        offset_angle = target_angle + rng.integers(-135, 135)

        # Calculate the start position by the sampled angle
        # Code variant A
        # x = spawn_radius * math.cos(math.radians(angle)) + 336 // 2
        # y = spawn_radius * math.sin(math.radians(angle)) + 336 // 2
        # self.start_position = (int(x), int(y))
        # Code variant B
        self.spawn_location = center + Vector2(self.spawn_radius, 0).rotate(start_angle)
        self.current_location = self.spawn_location
        # Calculate target location
        self.target_location = center + Vector2(self.spawn_radius, 0).rotate(target_angle)
        # Calculate offset location
        self.offset_location = center + Vector2(self.spawn_radius, 0).rotate(offset_angle)

    def draw(self, surface):
        """Draw the spotlight on the given surface.

        Arguments:
            surface {pygame.Surface} -- The surface on which to draw the spotlight.
        """
        lerp_target = self.target_location.lerp(self.offset_location, self.t)
        self.current_location = self.spawn_location.lerp(lerp_target, self.t)
        pygame.draw.circle(surface, (255, 0, 0), (int(self.current_location.x), int(self.current_location.y)), self.radius)
        if self.has_border:
            pygame.draw.circle(surface, (255, 255, 255), (int(self.current_location.x), int(self.current_location.y)), self.radius, 1)
        self.t += self.speed
        if self.t >= 1.0:
            self.t = 1.0
            self.done = True

    def is_agent_inside(self, agent) -> bool:
        """Check if the agent is inside the spotlight.

        Arguments:
            agent {pygame.sprite.Sprite} -- The agent object to check for intersection.

        Returns:
            {bool} -- True if the agent is inside the spotlight, False otherwise.
        """
        distance = self.current_location.distance_to(agent.rect.center)
        if distance <= self.radius + agent.radius:
            return True
        return False

class Coin():
    def __init__(self, scale, location) -> None:
        """Initialize the Coin with the specified scale and location.

        Arguments:
            scale {float} -- The scale factor for the size of the coin.
            location {tuple} -- The (x, y) coordinates of the center of the coin.
        """
        self.scale = scale
        self.radius = int(10 * scale)
        self.location = location

    def draw(self, surface):
        """Draw the coin on the given surface.

        Arguments:
            surface {pygame.Surface} -- The surface on which to draw the coin.
        """
        pygame.draw.circle(surface, (255, 255, 0), self.location, self.radius)
        pygame.draw.circle(surface, (255, 165, 0), self.location, self.radius, int(2 * self.scale))

    def is_agent_inside(self, agent) -> bool:
        """Check if the agent is inside the coin.

        Arguments:
            agent {pygame.sprite.Sprite} -- The agent object to check for intersection.

        Returns:
            {bool} -- True if the agent is inside the coin, False otherwise.
        """
        location = Vector2(self.location)
        distance = location.distance_to(agent.rect.center)
        if distance <= self.radius + agent.radius:
            return True
        return False

class Exit():
    def __init__(self, location , scale) -> None:
        """Initialize the Exit with the specified location and scale.

        Arguments:
            location {tuple} -- The (x, y) coordinates of the center of the exit.
            scale {float} -- The scale factor for the size of the exit.
        """
        rect_dim = 20 * scale
        self.surface = pygame.Surface((rect_dim, rect_dim))
        self.surface.fill(255)
        self.surface.set_colorkey(255)
        self.rect = self.surface.get_rect()
        self.origin = self.rect.copy()
        self.scale = scale
        self.radius = 20 / 2 * scale
        self.color_open = (48, 141, 70)
        self.color_closed = (55, 55, 55)
        self.rounded_corners = (int(10 * scale), int(10 * scale), 0, 0)
        self.location = location
        self.open = True

    def draw(self, open = False):
        """Draw the exit on the given surface with the specified state (open or closed).

        Arguments:
            open {bool} -- True to draw the exit as open, False to draw it as closed (default).
        """
        if open != self.open:
            self.open = open
            self.rect.center = self.origin.center
            if open:
                pygame.draw.rect(self.surface, self.color_open, self.rect, 0, 0, *self.rounded_corners)
            else:
                pygame.draw.rect(self.surface, self.color_closed, self.rect, 0, 0, *self.rounded_corners)
            pygame.draw.rect(self.surface, 0, self.rect, int(2 * self.scale), 0, *self.rounded_corners)
            self.rect.center = self.location

    def is_agent_inside(self, agent) -> bool:
        """Check if the agent is inside the exit.

        Arguments:
            agent {pygame.sprite.Sprite} -- The agent object to check for intersection.

        Returns:
            {bool} -- True if the agent is inside the exit, False otherwise.
        """
        location = Vector2(self.location)
        distance = location.distance_to(agent.rect.center)
        if distance <= self.radius + agent.radius:
            return True
        return False

def get_tiled_background_surface(screen, screen_dim, tile_color, scale):
    """Create a tiled background surface with alternating colors.

    Arguments:
        screen {pygame.Surface} -- The main surface on which the background will be drawn.
        screen_dim {int} -- The width and height of the screen in pixels.
        tile_color {tuple} -- The RGB color tuple for one of the tile colors.
        scale {float} -- The scale factor for the size of the tiles.

    Returns:
        {pygame.Surface} -- The generated background surface.
    """
    background_surface = pygame.Surface((screen_dim, screen_dim))
    ts, w, h, c1, c2 = int(50 * scale), *screen.get_size(), (255, 255, 255), tile_color
    tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
    for rect, color in tiles:
        pygame.draw.rect(background_surface, color, rect)
    return background_surface

class Command():
    COMMANDS = {
        "right"     : (1, 0),
        "down"      : (0, 1),
        "left"      : (-1, 0),
        "up"        : (0, -1),
        "stay"      : (0, 0),
        "right_down": (1, 1),
        "right_up"  : (1, -1),
        "left_down" : (-1, 1),
        "left_up"   : (-1, -1),
    }

    def __init__(self, command_type, scale) -> None:
        """Initialize the Command object with a specific command type and scale factor.

        Arguments:
            command_type {str} -- The type of the command.
            scale {float} -- The scale factor for the size of the command surface.
        """
        assert command_type in Command.COMMANDS or command_type == ""
        self.scale = scale
        self.rect_dim = 88 * scale
        self.surface = pygame.Surface((self.rect_dim, self.rect_dim))
        self.surface.fill(0)
        self.surface.set_colorkey(0)
        self.rect = self.surface.get_rect()

        # Draw command symbol
        line_width = int(8 * scale)
        if command_type == "stay":
            radius = self.rect_dim // 2 - 4 * scale
            x = self.rect_dim - 12 * scale
            y = self.rect_dim // 2 - 8 * scale
            pygame.draw.circle(self.surface, (255, 255, 255), (radius, radius), radius=radius, width=line_width)
            pygame.draw.line(self.surface, (255, 255, 255), (0, y), (x, y), width=line_width)
        elif len(command_type) > 0:
            # Draw arrow that points right
            x1 = 2 * scale
            x2 = 80 * scale
            y1 = 40 * scale
            y2 = 0
            pygame.draw.line(self.surface, (255, 255, 255), (x1, y1), (x2, y1), line_width)
            pygame.draw.line(self.surface, (255, 255, 255), (x2, y1), (y1, y2), line_width)
            pygame.draw.line(self.surface, (255, 255, 255), (x2, y1), (y1, x2), line_width)
            # Determine rotation
            angle = 0
            if command_type == "left":
                angle = 180
            elif command_type == "down":
                angle = 270
            elif command_type == "up":
                angle = 90
            elif command_type == "right_down":
                angle = 315
            elif command_type == "right_up":
                angle = 45
            elif command_type == "left_down":
                angle = 225
            elif command_type == "left_up":
                angle = 135
            # self.surface, self.rect = self.rotate(angle)
            self.surface = pygame.transform.rotate(self.surface, angle)
            self.rect = self.surface.get_rect(center = self.rect.center)

class MortarTile():
    def __init__(self, dim, scale, global_position, surface_rect) -> None:
        """Initialize the MortarTile object with specific dimensions, scale, and position.

        Arguments:
            dim {int} -- The width and height of the mortar tile in pixels.
            scale {float} -- The scale factor for the size of the tile.
            global_position {tuple} -- The global (x, y) position of the tile on the main surface.
            surface_rect {tuple} -- The rectangle representing the dimensions and position of the main surface.
        """
        self.dim = dim
        self.scale = scale
        self.surface = pygame.Surface((dim, dim))
        self.rect = self.surface.get_rect()
        self.global_position = global_position
        self.local_position = (global_position[0] - surface_rect[0], global_position[1] - surface_rect[1])
        self.normalized_pos = (self.local_position[0] // self.dim, self.local_position[1] // self.dim)
        self.blue = (21, 43, 77)
        self.light_blue = (29, 60, 107)
        self.red = (81, 18, 26)
        self.light_red = (112, 24, 36)
        self.is_blue = True
        pygame.draw.rect(self.surface, self.blue, ((0, 0, dim, dim)))
        pygame.draw.rect(self.surface, self.light_blue, ((0, 0, dim, dim)), width=int(4 * scale))

    def toggle_color(self, on, change_color = True):
        """Toggle the color of the mortar tile between blue and red.

        Arguments:
            on {bool} -- A flag indicating whether to set the tile color to red.
            change_color {bool} -- A flag indicating whether to change the color on the tile surface (default: True).
        """
        self.is_blue = not self.is_blue
        if change_color:
            c1 = self.blue if not on else self.red
            c2 = self.light_blue if not on else self.light_red
            pygame.draw.rect(self.surface, c1, ((0, 0, self.dim, self.dim)))
            pygame.draw.rect(self.surface, c2, ((0, 0, self.dim, self.dim)), width=int(4 * self.scale))

class MortarArena():
    def __init__(self, scale, arena_size) -> None:
        """Initialize the MortarArena object with a specific scale and size.

        Arguments:
            scale {float} -- The scale factor for the size of the arena and tiles.
            arena_size {int} -- The number of tiles along one side of the square arena.
        """
        self.scale = scale
        self.arena_size = arena_size
        self.tile_dim = 56 * scale
        self.rect_dim = self.tile_dim * arena_size
        self.surface = pygame.Surface((self.rect_dim, self.rect_dim))
        self.rect = self.surface.get_rect()
        self.local_center = self.rect.center
        self.tiles = [[] for _ in range(arena_size)]
        self.tiles_on = False
        for i in range(self.arena_size):
            x = self.tile_dim * i
            for j in range(self.arena_size):
                y = self.tile_dim * j
                tile = MortarTile(self.tile_dim, scale, (x, y), self.rect)
                self.tiles[i].append(tile)
                self.surface.blit(tile.surface, tile.global_position)

    def get_tile_global_position(self, flat_tile_id):
        """Get the global (x, y) position of a tile based on its flattened ID.

        Arguments:
            flat_tile_id {int} -- The flattened ID of the tile in the arena.

        Returns:
            {tuple} -- The global (x, y) position of the tile.
        """
        x = flat_tile_id // self.arena_size
        y = flat_tile_id % self.arena_size
        tile = self.tiles[x][y]
        pos = tile.global_position
        return pos

    def toggle_tiles(self, target_tile = None, change_color = True):
        """Toggle the colors of the tiles in the arena.

        Keyword Arguments:
            target_tile {tuple} -- The (x, y) coordinates of the tile to be toggled (default: None).
            change_color {bool} -- A flag indicating whether to change the color of the tiles (default: True).
        """
        self.tiles_on = target_tile is not None
        for i in range(self.arena_size):
            for j in range(self.arena_size):
                if self.tiles_on:
                    if not target_tile == (i, j):
                        tile = self.tiles[i][j]
                        tile.toggle_color(self.tiles_on, change_color)
                        self.surface.blit(tile.surface, tile.global_position)
                else:
                    tile = self.tiles[i][j]
                    tile.toggle_color(self.tiles_on, change_color)
                    self.surface.blit(tile.surface, tile.global_position)

    def to_grid(self):
        """Convert the positions of the tiles to a grid of GridPosition objects.

        Returns:
            {list} -- A 2D list of GridPosition objects representing the positions of the tiles in the arena.
        """
        grid = [[] for _ in range(self.arena_size)]
        translate_x = self.rect.center[0] - self.local_center[0] + self.tile_dim // 2
        translate_y = self.rect.center[1] - self.local_center[1] + self.tile_dim // 2
        for i in range(self.arena_size):
            for j in range(self.arena_size):
                tile = self.tiles[i][j]
                grid[i].append(GridPosition(tile.global_position[0] + translate_x, tile.global_position[1] + translate_y, i, j))
        return grid

def calc_max_episode_steps(command_count, show_duration, show_delay, execution_duration, execution_delay):
    """Calculates the maximum number of steps one episode can last.

    Arguments:
        command_count {int} -- Max number of commands
        show_duration {int} -- Max number of steps a command is shown
        show_delay {int} -- Max number of steps between showing commands
        execution_duration {int} -- Max number of steps of moving to the target tile
        execution_delay {int} -- Max number of steps to validate the current tile

    Returns:
        {int} -- Returns the maximum number of steps that one episode can last
    """
    clue_task_steps = (show_duration + show_delay) * command_count
    act_task_steps = (execution_duration + execution_delay) * command_count
    act_task_steps = act_task_steps - execution_delay + 1
    return clue_task_steps + act_task_steps

class Node():
    def __init__(self, i, j, is_wall = False):
        """Initialize the Node object with specific coordinates and wall status.

        Arguments:
            i {int} -- The x-coordinate of the node in the grid.
            j {int} -- The y-coordinate of the node in the grid.
            is_wall {bool} -- A flag indicating whether the node is a wall (default: False).
        """
        self.x, self.y = i, j
        self.f_cost, self.g_cost, self.h_cost = 0, 0, 0
        self.neighbors = []
        self.diagonal_neighbors = []
        self.previous_node = None
        self.next_node = None
        self.is_wall = is_wall
        self.reward_visited = False
        self.stamina_visited = False

    def add_neighbors(self, grid, num_columns, num_rows):
        """Add neighboring nodes to the current node.

        Arguments:
            grid {list} -- A 2D list representing the grid containing nodes.
            num_columns {int} -- The number of columns in the grid.
            num_rows {int} -- The number of rows in the grid.
        """
        if self.x < num_columns - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < num_rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])
        # add diagonal neighbors
        if self.x < num_columns - 1 and self.y < num_rows - 1:
            self.diagonal_neighbors.append(grid[self.x+1][self.y+1])
        if self.x > 0 and self.y > 0:
            self.diagonal_neighbors.append(grid[self.x-1][self.y-1])
        if self.x < num_columns - 1 and self.y > 0:
            self.diagonal_neighbors.append(grid[self.x+1][self.y-1])
        if self.x > 0 and self.y < num_rows - 1:
            self.diagonal_neighbors.append(grid[self.x-1][self.y+1])

    def draw_to_surface(self, surface, tile_dim, color):
        """Draw the node on a surface with a specific color.

        Arguments:
            surface {pygame.Surface} -- The surface on which the node will be drawn.
            tile_dim {int} -- The width and height of each tile in the grid in pixels.
            color {tuple} -- The RGB color tuple for the node.
        """
        if self.is_wall:
            color = (255, 0, 0)
        pygame.draw.rect(surface, color, (self.x * tile_dim, self.y * tile_dim, tile_dim, tile_dim))

class EndlessMysteryPath():
    def __init__(self, num_columns, num_rows, tile_dim, rng, num_initial_segments) -> None:
        """Initialize the EndlessMysteryPath object.

        Arguments:
            num_columns {int} -- The number of columns in each segment of the mystery path.
            num_rows {int} -- The number of rows in each segment of the mystery path.
            tile_dim {int} -- The width and height of each tile in pixels for rendering.
            rng {numpy.random.Generator} -- The random number generator used for sampling positions.
            num_initial_segments {int} -- The number of initial segments to create for the path.
        """
        self.path = []
        self.num_segments = 0
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.rng = rng
        self.start_position, self.end_position = None, None

        for _ in range(num_initial_segments):
            self.add_path_segment()

        self.gen_surface(tile_dim)
        self.segment_length = self.num_columns + 1 # +1 for the transition tile

        # The first node of the path shall not yield any reward
        self.path[0][0].reward_visited = True

    def get_segment(self, segment_index):
        """Get the segment at the specified index from the mystery path.

        Arguments:
            segment_index {int} -- The index of the segment to retrieve.

        Returns:
            {list} -- A list of nodes representing the segment at the specified index.
        """
        return self.path[segment_index]

    def render_path(self):
        """Render the entire mystery path and save it as an image."""
        tile_size = 50
        surface = pygame.Surface(((self.num_columns * self.num_segments + self.num_segments) * tile_size, self.num_rows * tile_size))
        surface.fill((0, 0, 0))
        for segment in self.path:
            for node in segment:
                pygame.draw.rect(surface, (255, 255, 255), (node.x * tile_size, node.y * tile_size, tile_size, tile_size))
        # path surface to image
        pygame.image.save(surface, "path.png")

    def gen_surface(self, tile_size):
        """Generate a surface representing the mystery path for rendering.

        Arguments:
            tile_size {int} -- The width and height of each tile in pixels for rendering.
        """
        surface = pygame.Surface(((self.num_columns * self.num_segments + self.num_segments) * tile_size, self.num_rows * tile_size))
        surface.fill((0, 0, 0))
        surface.set_colorkey((0, 0, 0))
        surface.set_alpha(200)
        for segment in self.path:
            for node in segment:
                pygame.draw.rect(surface, (255, 255, 255), (node.x * tile_size, node.y * tile_size, tile_size, tile_size))
        self.surface = surface

    def add_path_segment(self):
        """Add a new segment to the mystery path."""
        # Determine start position
        if self.start_position is None:
            self.start_position = (0, self.rng.integers(0, self.num_rows))
        else:
            # Convert end position to start position
            self.start_position = (0, self.end_position[1])

        # Sample end position
        self.end_position = (self.num_rows - 1, self.rng.integers(0, self.num_rows))

        # Build path segment
        mystery_path = MysteryPath(self.num_columns, self.num_rows, self.start_position, self.end_position, self.rng)

        # Update x position of nodes depending on self.num_segments (and transition nodes)
        for node in mystery_path.path:
            if self.num_segments == 0:
                node.x += self.num_segments * self.num_rows
            else:
                node.x += self.num_segments * self.num_rows + self.num_segments

        # Increment the number of segments
        self.num_segments += 1

        # Add a transition node to the path that increments the x position
        # This is done to avoid too many neighboring nodes for the end and start nodes
        transition_node = Node(self.end_position[0] + self.num_segments + (self.num_segments - 1) * self.num_rows, self.end_position[1])
        transition_node.previous_node = mystery_path.path[0]
        mystery_path.path.insert(0, transition_node)

        # Concatenate the new segment to the entire path
        mystery_path.path.reverse()
        self.path.append(mystery_path.path)

        # Set the previous node reference of the first node of the new segment
        if len(self.path) > 1:
            self.path[self.num_segments - 1][0].previous_node = self.path[self.num_segments - 2][-1]

        # Set the next node reference for every node in the new segment
        for i in range(len(self.path[self.num_segments - 1]) - 1):
            self.path[self.num_segments - 1][i].next_node = self.path[self.num_segments - 1][i + 1]

        # Set the next node of the last node of the previous segment
        if self.num_segments > 1:
            self.path[self.num_segments - 2][-1].next_node = self.path[self.num_segments - 1][0]

class MysteryPath():
    def __init__(self, num_columns, num_rows, start_position, end_position, rng) -> None:
        """Initialize the MysteryPath object and generate the path.

        Arguments:
            num_columns {int} -- The number of columns in the grid of nodes for the mystery path.
            num_rows {int} -- The number of rows in the grid of nodes for the mystery path.
            start_position {tuple} -- The starting position (x, y) of the mystery path.
            end_position {tuple} -- The ending position (x, y) of the mystery path.
            rng {numpy.random.Generator} -- The random number generator used for generating walls and A* algorithm.
        """
        path_found = False
        self.grid = []
        open_set, closed_set = [], []
        self.path = []
        self.wall_nodes = []

        # Instantiate all nodes
        for i in range(num_columns):
            column = []
            for j in range(num_rows):
                is_wall = False
                # Randomly add walls to the inside of the grid
                if i > 0 and i < num_columns - 2 and j > 0 and j < num_rows - 2:
                    if rng.integers(0, 100) < 33:
                        is_wall = True
                node = Node(i,j,is_wall)
                column.append(node)
                if is_wall:
                    self.wall_nodes.append(node)
            self.grid.append(column)

        # Set neighbors
        for i in range(num_columns):
            for j in range(num_rows):
                self.grid[i][j].add_neighbors(self.grid, num_columns, num_rows)

        # Set start and end nodes
        start_node = self.grid[start_position[0]][start_position[1]]
        end_node = self.grid[end_position[0]][end_position[1]]

        # Add walls to the outer edge of the grid
        # Gather all nodes, but select only nodes that are not adjacent (also diagonally) to a wall
        # Ensure that the start and end nodes (plus neighbors) are not added to this set of nodes
        outer_nodes = []
        for i in range(num_columns):
            for j in range(num_rows):
                if i == 0 or i == num_columns - 1 or j == 0 or j == num_rows - 1:
                    node = self.grid[i][j]
                    if i != start_position[0] or j != start_position[1]:
                        if i != end_position[0] or j != end_position[1]:
                            if node not in start_node.neighbors and node not in end_node.neighbors:
                                adjacent_to_wall = False
                                for neighbor in node.neighbors:
                                    if neighbor.is_wall:
                                        adjacent_to_wall = True
                                        break
                                if not adjacent_to_wall:
                                    for neighbor in node.diagonal_neighbors:
                                        if neighbor.is_wall:
                                            adjacent_to_wall = True
                                            break
                                if not adjacent_to_wall:
                                    outer_nodes.append(node)
        
        # Randomly select nodes from the outer node list and turn them into walls
        for i in range(rng.choice([4, 8])):
            if len(outer_nodes) > 0:
                node = rng.choice(outer_nodes)
                node.is_wall = True
                self.wall_nodes.append(node)
                outer_nodes.remove(node)

        # A* algorithm to procedurally generate a path, which is not necessarily the shortest path
        # Add start node to open set
        open_set.append(start_node)
        while not path_found:
            if len(open_set) > 0:
                # Pick the most promising node from the open set
                winner_node_id = 0
                for i in range(len(open_set)):
                    if open_set[i].f_cost < open_set[winner_node_id].f_cost:
                        winner_node_id = i
                        break # maybe don't, or sample break because there might be multiple shortest paths
                current_node = open_set[winner_node_id]

                # If the end node is reached, trace back the nodes to retrieve the path
                if current_node == end_node:
                    self.path.append(end_node)
                    temp = current_node
                    while temp.previous_node:
                        self.path.append(temp.previous_node)
                        temp = temp.previous_node 
                    path_found = True
                else:
                    open_set.remove(current_node)
                    closed_set.append(current_node)

                    for neighbor in current_node.neighbors:
                        if neighbor in closed_set or neighbor.is_wall:
                            continue
                        g = current_node.g_cost + rng.integers(1, 9)#g_cost_noise[current_node.x, current_node.y]

                        new_path = False
                        if neighbor in open_set:
                            if g < neighbor.g_cost:
                                neighbor.g = g
                                new_path = True
                        else:
                            neighbor.g_cost = g
                            new_path = True
                            open_set.append(neighbor)

                        if new_path:
                                neighbor.h_cost = self.heuristic(neighbor, end_node)
                                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                                neighbor.previous_node = current_node
            else:
                raise Exception("No valid path found")

    def heuristic(self, a, b):
        """Calculate the heuristic (Manhattan) distance between two nodes.

        Arguments:
            a {Node} -- The first node.
            b {Node} -- The second node.

        Returns:
            {float} -- The heuristic distance between the two nodes.
        """
        return math.sqrt((a.x - b.x)**2 + abs(a.y - b.y)**2)

    def draw_to_surface(self, surface, tile_dim, show_origin, show_goal, show_path = False, show_walls = False):
        """Draw the path and walls on a given surface.

        Arguments:
            surface {pygame.Surface} -- The surface on which to draw the path and walls.
            tile_dim {int} -- The width and height of each tile in pixels for rendering.
            show_origin {bool} -- Whether to draw the starting node in the path.
            show_goal {bool} -- Whether to draw the ending node in the path.
            show_path {bool} -- Whether to draw all nodes in the path except the starting and ending nodes. (default is False)
            show_walls {bool} -- Whether to draw the wall nodes. (default is False)
        """
        for n, node in enumerate(self.path):
            if n == 0 and show_goal:
                color = (0, 255, 0)
                node.draw_to_surface(surface, tile_dim, color)
            elif n == len(self.path) - 1 and show_origin:
                color = (0, 0, 255)
                node.draw_to_surface(surface, tile_dim, color)
            elif n > 0 and n < len(self.path) - 1 and show_path:
                color = (255, 255, 255)
                node.draw_to_surface(surface, tile_dim, color)
        
        if show_walls:
            for node in self.wall_nodes:
                node.draw_to_surface(surface, tile_dim, color)

    def to_grid(self, cell_dim):
        """Convert the path grid to a grid of positions.

        Arguments:
            cell_dim {int} -- The size of each cell.

        Returns:
            {list} -- A 2D list representing the grid of positions.
        """
        size = len(self.grid)
        cells = [[] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                cells[i].append(GridPosition(cell_dim * i + cell_dim // 2, cell_dim * j + cell_dim // 2, i, j))
        return cells

def draw_icy_surface(tile_dim):
    """Create a surface with a frozen lake-like appearance.

    Arguments:
        tile_dim {int} -- The width and height of the surface.

    Returns:
        {pygame.Surface} -- The created surface.
    """
    border_width = 1
    # Init surface
    surface = pygame.Surface((tile_dim, tile_dim))
    # Fill surface light blue (like a frozen lake)
    surface.fill((125, 177, 250))
    # Draw border
    pygame.draw.rect(surface, (210, 210, 210), (0, 0, tile_dim, tile_dim), border_width)
    # Return surface
    return surface

def draw_column_tile_surface(tile_dim, num_tiles):
    """Create a surface composed of multiple icy surfaces stacked.

    Arguments:
        tile_dim {int} -- The width and height of each tile.
        num_tiles {int} -- The number of tiles to stack.

    Returns:
        {pygame.Surface} -- The created surface.
    """
    tile_dim = int(tile_dim)
    # Init surface
    surface = pygame.Surface((tile_dim, tile_dim * num_tiles))
    # Fill surface with black
    surface.fill((0, 0, 0))
    for i in range(num_tiles):
        surface.blit(draw_icy_surface(tile_dim), (0, i * tile_dim))
    # Return surface
    return surface

class GridPosition():
    def __init__(self, x, y, i, j) -> None:
        self.x = x
        self.y = y
        self.i = i
        self.j = j
