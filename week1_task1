import pygame
pygame.init()
size = width, height = 400, 200
screen = pygame.display.set_mode(size)
def draw():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("Calibri bold", 54)
    text = font.render("Hello Pygame", 1, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.flip()
pygame.quit()
