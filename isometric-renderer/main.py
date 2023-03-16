import pygame
from renderer import Renderer


def update(clock):
    events = pygame.event.get()
    dt = clock.tick(60)

    pygame.display.set_caption(f"Isometric Renderer Test | {clock.get_fps():.2f}")
    for event in events:
        if event.type == pygame.QUIT:
            raise SystemExit


def draw(screen, renderer: Renderer):
    screen.fill("black")
    renderer.draw(screen)
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 150), pygame.SCALED)
    clock = pygame.time.Clock()

    world_array = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    tile = pygame.image.load("assets/tile.png").convert_alpha()
    renderer = Renderer(world_array, tile)

    while True:
        update(clock)
        draw(screen, renderer)


if __name__ == "__main__":
    main()
