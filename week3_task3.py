import pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
player_rect = pygame.Rect(width // 2, height - 60, 50, 50)
player_speed = 5
enemy_width = 50
enemy_height = 50
enemies = []
enspeed = 3
delay_spawn = 60
timer = 0
lives = 3
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if player_rect.x < 0:
        player_rect.x = 0
    if player_rect.x > width - player_rect.width:
        player_rect.x = width - player_rect.width
    timer += 1
    if timer >= delay_spawn:
        timer = 0
        enemies.append(pygame.Rect(player_rect.x, 0, 50, 50))
    for i in enemies:
        i.y += enspeed
        if i.y > height:
            enemies.remove(i)
    for i in enemies:
        if player_rect.colliderect(i):
            lives -= 1
            player_rect.x = width // 2
            player_rect.y = height - 60
            if lives <= 0:
                running = False
    screen.fill((0, 0, 0))
    for i in enemies:
        pygame.draw.rect(screen, (255, 0, 0), i)
    pygame.draw.rect(screen, (0, 0, 255), player_rect)
    lives_text = font.render(f"Lives: {lives}", True, (0, 255, 0))
    screen.blit(lives_text, (0, 0))
    pygame.display.flip()
    clock.tick(60)
screen.fill((0, 0, 0))
game_over_text = font.render("Game Over", True, (0, 255, 0))
screen.blit(game_over_text, (width // 2 - 100, height // 2 - 20))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
