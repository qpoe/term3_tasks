import pygame
pygame.init()
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("Calibri bold", 54)
text = "Hello Pygame Click Anywhere Highlight"
words = text.split()
word_positions = []
x, y = 100, 300
spacing = 10
for word in words:
    text_surface = font.render(word, True, (100, 255, 100))
    word_positions.append((word, text_surface, (x, y)))
    x += text_surface.get_width() + spacing
highlighted_word = None
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for word, text_surface, (word_x, word_y) in word_positions:
                word_w, word_h = text_surface.get_size()
                if word_x <= mouse_x <= word_x + word_w and word_y <= mouse_y <= word_y + word_h:
                    highlighted_word = word
                    break
    for word, text_surface, (word_x, word_y) in word_positions:
        if word == highlighted_word:
            pygame.draw.rect(screen, "yellow", (word_x - 5, word_y - 5, text_surface.get_width() + 10, text_surface.get_height() + 10))
        screen.blit(text_surface, (word_x, word_y))
    pygame.display.flip()
pygame.quit()
