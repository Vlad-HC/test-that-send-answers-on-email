import pygame

pygame.init()

# Параметри вікна
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TextBox Example")

# Шрифти та кольори
FONT = pygame.font.Font(None, 24)
TEXT_COLOR = (255, 255, 255)
BG_COLOR = (30, 30, 30)


# Функція для розбиття тексту на рядки
def wrap_text(text, font, max_width):
    words = text.split()  # Розбиваємо текст на слова
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        text_width, _ = font.size(test_line)

        if text_width > max_width:  # Якщо рядок перевищує ширину
            lines.append(current_line.strip())  # Додаємо поточний рядок у список
            current_line = word + " "  # Починаємо новий рядок
        else:
            current_line = test_line  # Додаємо слово до рядка

    lines.append(current_line.strip())  # Додаємо останній рядок
    return lines


def draw_textbox(text, x, y, width, height):
    pygame.draw.rect(screen, (50, 50, 50), (x, y, width, height), border_radius=5)
    lines = wrap_text(text, FONT, width - 10)  # 10 пікселів на відступи

    for i, line in enumerate(lines):
        text_surface = FONT.render(line, True, TEXT_COLOR)
        screen.blit(text_surface, (x + 5, y + 5 + i * 20))  # Відступ 5px


running = True
text = "This is a sample text that should be wrapped inside the textbox when it reaches the max width."

while running:
    screen.fill(BG_COLOR)
    draw_textbox(text, 50, 50, 400, 200)  # Координати та розмір текстового поля

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
