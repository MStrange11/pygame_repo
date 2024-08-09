import pygame
import pygame_gui
import sys

pygame.init()

WIDTH, HEIGHT = 800, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input in PyGame | BaralTech")

manager = pygame_gui.UIManager((WIDTH, HEIGHT), "theme.json")

# Text input field
text_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 300), (400, 50)),
    manager=manager,
    object_id='#text'
)
text_input.visible = 0  # Initially hide the text input field

# Create an icon button to toggle the visibility of the input surface
toggle_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (50, 50)),
    text='Icon',
    manager=manager
)

text_box = pygame_gui.elements.UITextBox(
     html_text="This is an <effect id=test>EARTHQUAKE</effect>",
     relative_rect=pygame.Rect(100, 100, 200, 50),
     manager=manager)

clock = pygame.time.Clock()

def show_user_name(user_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill("white")

        new_text = pygame.font.SysFont("bahnschrift", 100).render(f"Hello, {user_name}", True, "black")
        new_text_rect = new_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        SCREEN.blit(new_text, new_text_rect)

        clock.tick(60)
        pygame.display.update()

def get_user_name():
    while True:
        UI_REFRESH_RATE = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == toggle_button:
                text_input.visible = not text_input.visible  # Toggle visibility of the text input
                # text_box.set_active_effect(pygame_gui.TEXT_EFFECT_BOUNCE, effect_tag='test')
                text_box.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)

            if text_input.visible and (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_element == text_input):
                show_user_name(event.text)

            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)
        SCREEN.fill("white")

        manager.draw_ui(SCREEN)  # Draw all UI elements managed by the manager

        pygame.display.update()

get_user_name()
