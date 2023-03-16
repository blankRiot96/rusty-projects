import pygame


class Renderer:
    """A renderer to handle the rendering of isometric tiles."""

    def __init__(self, world_array: list[list[int]], tile: pygame.Surface) -> None:
        self.world_array = world_array
        self.rows = len(self.world_array)
        self.cols = len(self.world_array[0])
        self.tile = tile.copy()
        self.tile_rect = self.tile.get_rect()

    def transform(self, x, y) -> tuple[int, int]:
        """Transforms isometric coordinate to screen space"""

        screen_x = (x - y) * (self.tile_rect.width / 2)
        screen_y = (x + y) * (self.tile_rect.height / 2)

        return screen_x, screen_y

    def draw(self, screen: pygame.Surface) -> None:
        for y in range(self.cols):
            for x in range(self.rows):
                if self.world_array[x][y] != 1:
                    continue
                screen_x, screen_y = self.transform(x, y)
                screen.blit(self.tile, (screen_x, screen_y))
