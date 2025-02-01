import pygame
import random
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
player_rect = pygame.Rect(width // 2, height - 60, 50, 50)
speed = 5
coin_radius = 15
coins = []
delay = 60
timer = 0
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if player_rect.x < 0:
        player_rect.x = 0
    if player_rect.x > width - player_rect.width:
        player_rect.x = width - player_rect.width
    timer += 1
    if timer >= delay:
        timer = 0
        coin_x = random.randint(coin_radius, width - coin_radius)
        coins.append((coin_x, 0))
    for i in range(len(coins)):
        coins[i] = (coins[i][0], coins[i][1] + 2)

    for coin in coins:
        collide_p = (coin[0], coin[1] + coin_radius)
        if player_rect.collidepoint(collide_p):
            coins.remove(coin)
            score += 1
    coins = [coin for coin in coins if coin[1] < height]
    screen.fill((0, 0, 0))
    for coin in coins:
        pygame.draw.circle(screen, "yellow", coin, coin_radius)
    pygame.draw.rect(screen, (0, 0, 255), player_rect)
    score_text = font.render(f"Score: {score}", True, (0, 255, 0))
    screen.blit(score_text, (0, 0))
    pygame.display.flip()
    clock.tick(60)
screen.fill((0, 0, 0))
game_over_text = font.render(f"Game Over! Final Score: {score}", True, (0, 255, 0))
screen.blit(game_over_text, (width // 2 - 150, height // 2 - 20))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
