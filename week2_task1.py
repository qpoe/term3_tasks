import pygame
pygame.init()
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (80, 50))
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
x, y = 250, 250
speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    screen.fill((0, 0, 0))
    screen.blit(car, (x, y))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
