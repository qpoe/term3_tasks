import pygame
pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
image = pygame.image.load("boom.png")
image_rect = image.get_rect()
screen.blit(image, image_rect)
scale_factor = 1.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scale_factor += 0.1
            elif event.button == 5:
                scale_factor -= 0.1
    if scale_factor < 0:
        scale_factor = 0.1
    scaled_image = pygame.transform.scale(
        image, (int(image_rect.width * scale_factor), int(image_rect.height * scale_factor))
    )
    scaled_image_rect = scaled_image.get_rect(center=image_rect.center)
    screen.fill((0, 0, 0))
    screen.blit(scaled_image, scaled_image_rect)
    pygame.display.flip()
pygame.quit()
