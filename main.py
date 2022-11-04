import pygame
import sys

# my comment


"""
Seth: TEST COMMIT AND PUSH
"""


# initializes the game and pygame fonts
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Fraction Distraction")

# initializes game sound effects
button_sound = pygame.mixer.Sound("Assets/button.mp3")

# basic global values
screen_width = 1280
screen_height = 720
mouse_click = False

main_screen = pygame.display.set_mode((screen_width, screen_height))  # creates the main screen of the game

# loads in the assets (background and fonts)
start_background = pygame.image.load("Assets/start_bg.jpg")
big_font = pygame.font.Font("Assets/zx_spectrum.ttf", 70)
small_font = pygame.font.Font("Assets/zx_spectrum.ttf", 45)


def draw_text(text, font, color, surface, x, y):
    """ creates a text box

    @param text: string of the text
    @param font: font of the text, should be in the .ttf file format
    @param color: color of the text, can be in r,g,b or string: https://www.discogcodingacademy.com/turtle-colours
    @param surface: the screen that the text will be on
    @param x: x-position of the text - middle of the text box
    @param y: y-position of the text - middle of the text bos
    """

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def menu(click, message, top_button, bottom_button):
    """ creates the menu screen for the game

    @param click: state of the mouse, True if player presses Mouse 1
    @param message: string for the message at the top of the screen
    @param top_button: string for the text for the top button
    @param bottom_button: string for the text for the bottom button
    """

    """---------------------------------SETUP-------------------------------"""
    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse

    # Rects for the two buttons
    start_button = pygame.Rect(screen_width / 2 - 185, screen_height / 2 - 80, 370, 80)
    tutorial_button = pygame.Rect(screen_width / 2 - 185, screen_height / 2 + 40, 370, 80)

    """"----------------------------------LOOP-------------------------------"""
    while True:
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        # Check for mouse over and mouse click on the start button, button changes color on mouse over
        if start_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (64, 128, 230), start_button, 0, 5)
            if click:
                button_sound.play()
                print("Betting Screen")
                "TO DO"
        else:
            pygame.draw.rect(main_screen, (46, 102, 191), start_button, 0, 5)

        # Check for mouse over and mouse click on the quit button, button changes color on mouse over
        if tutorial_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), tutorial_button, 0, 5)
            if click:
                button_sound.play()
                print("Tutorial Screen")
                "TO DO"
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), tutorial_button, 0, 5)

        # Draws text on the menu screen
        draw_text(message, big_font, (255, 255, 255), main_screen, screen_width / 2, screen_height / 2 - 170)
        draw_text(top_button, small_font, (255, 255, 255), main_screen, screen_width / 2, screen_height / 2 - 40)
        draw_text(bottom_button, small_font, (255, 255, 255), main_screen, screen_width / 2, screen_height / 2 + 80)

        click = False  # resets the click event, prevents one click -> two actions

        # Checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    menu(mouse_click, "Fraction Distraction", "Enter!", "Tutorial")
