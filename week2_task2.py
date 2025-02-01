import pygame
pygame.init()
bomb = pygame.image.load("bomb2.png")
boom = pygame.image.load("boom.png")
bomb = pygame.transform.scale(bomb, (80, 80))
boom = pygame.transform.scale(boom, (80, 80))
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
bombs = [
    {"pos": (100, 150), "image": bomb, "exploded": False},
    {"pos": (250, 150), "image": bomb, "exploded": False},
    {"pos": (400, 150), "image": bomb, "exploded": False}
]
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for bomb_obj in bombs:
                x, y = bomb_obj["pos"]
                if x <= mouse_x <= x + 80 and y <= mouse_y <= y + 80:
                    bomb_obj["image"] = boom
                    bomb_obj["exploded"] = True
    for bomb_obj in bombs:
        screen.blit(bomb_obj["image"], bomb_obj["pos"])
    pygame.display.flip()
pygame.quit()
