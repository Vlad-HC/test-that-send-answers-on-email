import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("InputLabel Example")
clock = pygame.time.Clock()

# Fonts and Colors
FONT = pygame.font.Font(None, 50)
COLOR_ACTIVE = (255, 255, 255)  # White when active
COLOR_INACTIVE = (150, 150, 150)  # Gray when inactive
COLOR_TEXT = (0, 0, 0)  # Black text

# Input Box Setup
input_box = pygame.Rect(300, 250, 200, 50)  # x, y, width, height
color = COLOR_INACTIVE  # Initial color
active = False  # Box is not active at the start
text = ""  # Initial text

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check if clicked inside input box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active  # Toggle active state
            else:
                active = False
            color = COLOR_ACTIVE if active else COLOR_INACTIVE

        # Handle typing when active
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:  # Enter key
                print(f"Input Text: {text}")
                text = ""  # Clear input
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]  # Remove last character
            else:
                text += event.unicode  # Add typed character

    # Draw everything
    screen.fill((30, 30, 30))  # Dark background
    # Render text
    txt_surface = FONT.render(text, True, COLOR_TEXT)
    # Resize box if text is too long
    input_box.w = max(200, txt_surface.get_width() + 10)
    # Draw input box
    pygame.draw.rect(screen, color, input_box, border_radius=10)
    # Blit text on screen
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))

    pygame.display.flip()
    clock.tick(60)
