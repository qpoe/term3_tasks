import pygame
pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
surface = pygame.Surface((700, 700))
screen.fill((0, 0, 0))
font = pygame.font.SysFont("Calibri bold", 54)
text = font.render("Hello Pygame", 1, (100, 255, 100))
text_x = width // 2 - text.get_width() // 2
text_y = height // 2 - text.get_height() // 2
text_w = text.get_width()
text_h = text.get_height()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        text_x -= 5
    if keys[pygame.K_RIGHT]:
        text_x += 5
    if keys[pygame.K_UP]:
        text_y -= 5
    if keys[pygame.K_DOWN]:
        text_y += 5
    screen.fill((0, 0, 0))
    surface.fill((0, 0, 0))
    surface.blit(text, (text_x, text_y))
    pygame.draw.rect(surface, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)
    screen.blit(surface, (0, 0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
