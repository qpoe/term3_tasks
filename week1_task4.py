import pygame
pygame.init()
key_map = {
    pygame.K_a: 'a', pygame.K_b: 'b',
    pygame.K_c: 'c', pygame.K_d: 'd',
    pygame.K_e: 'e', pygame.K_f: 'f',
    pygame.K_g: 'g', pygame.K_h: 'h',
    pygame.K_i: 'i', pygame.K_j: 'j',
    pygame.K_k: 'k', pygame.K_l: 'l',
    pygame.K_m: 'm', pygame.K_n: 'n',
    pygame.K_o: 'o', pygame.K_p: 'p',
    pygame.K_q: 'q', pygame.K_r: 'r',
    pygame.K_s: 's', pygame.K_t: 't',
    pygame.K_u: 'u', pygame.K_v: 'v',
    pygame.K_w: 'w', pygame.K_x: 'x',
    pygame.K_y: 'y', pygame.K_z: 'z'
}
screen = pygame.display.set_mode((400, 100))
text = ""
# Define the font for the text
font = pygame.font.Font(None, 24)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            for key, character in key_map.items():
                if keys[key]:
                    text += character
            if keys[pygame.K_BACKSPACE]:
                text = text[:-1]
            elif keys[pygame.K_RETURN]:
                text = ""
    text_surface = font.render(text.upper(), True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text_surface, (20, 20))
    pygame.display.flip()
pygame.quit()
