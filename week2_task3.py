import pygame
pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
image = pygame.image.load("boom.png")
image_rect = image.get_rect(center=(width // 2, height // 2))
angle = 0
rotation_speed = 5
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += rotation_speed
    if keys[pygame.K_RIGHT]:
        angle -= rotation_speed
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)
    screen.fill((0, 0, 0))
    screen.blit(rotated_image, rotated_rect.topleft)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
