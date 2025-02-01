import pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
speed = 5
player_rect = pygame.Rect(width // 2 - 50, height // 2 - 50,
                          50, 50)
obstacles = [pygame.Rect(200, 150, 100, 100), pygame.Rect(500, 300, 150, 50),
             pygame.Rect(100, 400, 80, 80)]
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    next_x = player_rect.x
    next_y = player_rect.y
    if keys[pygame.K_LEFT]:
        next_x -= speed
    if keys[pygame.K_RIGHT]:
        next_x += speed
    if keys[pygame.K_UP]:
        next_y -= speed
    if keys[pygame.K_DOWN]:
        next_y += speed
    next_rect = pygame.Rect(next_x, next_y, 50, 50)
    collision = False
    for i in obstacles:
        if next_rect.colliderect(i):
            collision = True
            break
    if not collision:
        player_rect.x = next_x
        player_rect.y = next_y
    screen.fill((0, 0, 0))
    for i in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), i)
    pygame.draw.rect(screen, (0, 0, 255), player_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
