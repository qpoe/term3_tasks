import pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
player_rect = pygame.Rect(50, height - 60, 50, 50)
speed = 5
jump_speed = -15
gravity = 1
vertical_speed = 0
is_jumping = False
obstacle_width = 50
obstacle_height = 30
obstacles = [pygame.Rect(200, height - obstacle_height - 10, obstacle_width, obstacle_height),
             pygame.Rect(400, height - obstacle_height - 10, obstacle_width, obstacle_height),
             pygame.Rect(600, height - obstacle_height - 10, obstacle_width, obstacle_height)]
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                vertical_speed = jump_speed
    if is_jumping:
        vertical_speed += gravity
        player_rect.y += vertical_speed
        if player_rect.y >= height - 60:
            player_rect.y = height - 60
            is_jumping = False
            vertical_speed = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if player_rect.x < 0:
        player_rect.x = 0
    if player_rect.x > width - player_rect.width:
        player_rect.x = width - player_rect.width
    collision = False
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            collision = True
            break
    if collision:
        player_rect.x = 50
        player_rect.y = height - 60
        is_jumping = False
        vertical_speed = 0
    screen.fill((0, 0, 0))
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle)
    pygame.draw.rect(screen, (0, 0, 255), player_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
