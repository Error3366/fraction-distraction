import pygame
import sys

"""
Some cool code + new comment
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
big_font = pygame.font.Font("Assets/zx_spectrum.ttf", 50)
small_font = pygame.font.Font("Assets/zx_spectrum.ttf", 25)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.total_money = 100  # this can be changed later
        self.bet_won = 0
        self.money_won = 0
        self.money_on_table = 0
        self.items = []
        self.tutorials_completed = []

    def bet(self, total_bet):
        """ deducts and sets up the betting game

        :param total_bet: amount the Player wants to bet
        :return:
        """

        self.total_money -= total_bet
        self.money_on_table += total_bet

    def win(self, bet_type):
        """calculates the winnings"""

        self.total_money += self.money_on_table * (1.1 if bet_type == "small" else 1.3 if bet_type == "medium" else 1.5)
        self.money_on_table = 0


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


def universal_UI(home_button, quit_button, mx, my, click):
    """ creates the basic home button (top left) and quit button (top right)

    :param quit_button:
    :param home_button:
    :param mx:
    :param my:
    :param click:
    """

    if home_button.collidepoint((mx, my)):
        pygame.draw.rect(main_screen, (64, 128, 230), home_button, 0, 5)
        if click:  # calls the main_game function and starts the game
            button_sound.play()
            menu(mouse_click, "Fraction Distraction")
    else:
        pygame.draw.rect(main_screen, (46, 102, 191), home_button, 0, 5)

    if quit_button.collidepoint((mx, my)):
        pygame.draw.rect(main_screen, (64, 128, 230), quit_button, 0, 5)
        if click:  # calls the main_game function and starts the game
            button_sound.play()
            sys.exit()
    else:
        pygame.draw.rect(main_screen, (46, 102, 191), quit_button, 0, 5)

    draw_text("Home", small_font, (255, 255, 255), main_screen, 90, 50)
    draw_text("Quit", small_font, (255, 255, 255), main_screen, 1190, 50)


def menu(click, message):
    """ creates the menu screen for the game

    @param click: state of the mouse, True if player presses Mouse 1
    @param message: string for the message at the top of the screen
    """

    """---------------------------------SETUP-------------------------------"""
    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse

    # Rects for the two buttons
    start_button = pygame.Rect(screen_width / 2 - 420, screen_height / 2 - 80, 370, 80)
    tutorial_button = pygame.Rect(screen_width / 2 - 420, screen_height / 2 + 40, 370, 80)
    quit_button = pygame.Rect(screen_width / 2 + 50, screen_height / 2 + 40, 370, 80)
    shop_button = pygame.Rect(screen_width / 2 + 50, screen_height / 2 - 80, 370, 80)

    player = Player()
    print(player.total_money)
    print(player.bet(50))
    print(player.total_money)
    print(player.win("big"))
    print(player.total_money)

    """"----------------------------------LOOP-------------------------------"""
    while True:
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        # Check for mouse over and mouse click on the start button, button changes color on mouse over
        if start_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (64, 128, 230), start_button, 0, 5)
            if click:
                button_sound.play()
                betting_screen()

        else:
            pygame.draw.rect(main_screen, (46, 102, 191), start_button, 0, 5)

        # Check for mouse over and mouse click on the quit button, button changes color on mouse over
        if tutorial_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), tutorial_button, 0, 5)
            if click:
                button_sound.play()
                print("Tutorial Screen")
                tutorial_select("Select Tutorial")
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), tutorial_button, 0, 5)

        # Check for mouse over and mouse click on the quit button, button changes color on mouse over
        if quit_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), quit_button, 0, 5)
            if click:
                button_sound.play()
                print("Quit")
                sys.exit()
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), quit_button, 0, 5)

        # Check for mouse over and mouse click on the quit button, button changes color on mouse over
        if shop_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), shop_button, 0, 5)
            if click:
                button_sound.play()
                print("Shop")
                """INSERT SHOP HERE"""
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), shop_button, 0, 5)

        # Draws text on the menu screen
        draw_text(message, big_font, (255, 255, 255), main_screen, screen_width / 2, screen_height / 2 - 170)
        draw_text("Shop", small_font, (255, 255, 255), main_screen, screen_width / 2 + 230, screen_height / 2 - 40)
        draw_text("Betting", small_font, (255, 255, 255), main_screen, screen_width / 2 - 230, screen_height / 2 - 40)
        draw_text("Quit", small_font, (255, 255, 255), main_screen, screen_width / 2 + 230, screen_height / 2 + 80)
        draw_text("Tutorial", small_font, (255, 255, 255), main_screen, screen_width / 2 - 230, screen_height / 2 + 80)

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


# noinspection PyInterpreter
def tutorial_select(message):
    """ creates the level select screen where the user can pick between: easy, hard, 2-players

    @param message: string for the message at the top of the screen
    """

    """---------------------------------SETUP-------------------------------"""
    click = False  # resets the mouse click to avoid a bug where one click would trigger two events

    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse

    # Rects for the tutorial buttons
    add_button = pygame.Rect((screen_width // 2) - 455, (screen_height // 2) - 80, 370, 80)
    multiply_button = pygame.Rect((screen_width // 2) + 85, (screen_height // 2) - 80, 370, 80)
    lcd_button = pygame.Rect((screen_width // 2) - 185, (screen_height // 2) + 40, 370, 80)
    transform_button = pygame.Rect((screen_width // 2) - 455, (screen_height // 2) + 160, 370, 80)
    y_button = pygame.Rect((screen_width // 2) + 85, (screen_height // 2) + 160, 370, 80)
    home_button = pygame.Rect(30, 20, 120, 60)
    quit_button = pygame.Rect(1130, 20, 120, 60)

    """"----------------------------------LOOP-------------------------------"""
    while True:  # screen loop
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        universal_UI(home_button, quit_button, mx, my, click)

        # Check for mouse over and mouse click on the easy button, button changes color on mouse over
        if add_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), add_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Addition/Subtraction Tutorial')
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), add_button, 0, 5)

        # Check for mouse over and mouse click on the hard button, button changes color on mouse over
        if multiply_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), multiply_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Multiplication/Division Tutorial')

        else:
            pygame.draw.rect(main_screen, (196, 16, 16), multiply_button, 0, 5)

        # Check for mouse over and mouse click on the 2-player button, button changes color on mouse over
        if lcd_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), lcd_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Find LCD Tutorial')
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), lcd_button, 0, 5)

        if y_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), y_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Transform Fraction Tutorial')
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), y_button, 0, 5)

        if transform_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), transform_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                equation = ['6', 'x', '+', '3', 'y', '=', '9']

                tutorials('Find Y-intercept form Tutorial')

        else:
            pygame.draw.rect(main_screen, (196, 16, 16), transform_button, 0, 5)

        # Draws text on the tutorial menu screen
        draw_text(message, big_font, (255, 255, 255), main_screen, screen_width // 2, screen_height / 2 - 170)
        draw_text("Add/Subtract", small_font, (255, 255, 255), main_screen, (screen_width // 2) - 270,
                  screen_height / 2 - 40)
        draw_text("Multiply/Divide", small_font, (255, 255, 255), main_screen, (screen_width // 2) + 270,
                  screen_height / 2 - 40)
        draw_text("LCD", small_font, (255, 255, 255), main_screen, screen_width // 2, screen_height / 2 + 80)
        draw_text("Transform Fraction", small_font, (255, 255, 255), main_screen, (screen_width // 2) + 270,
                  screen_height / 2 + 200)
        draw_text("Y-Intercept Form", small_font, (255, 255, 255), main_screen, (screen_width // 2) - 270,
                  screen_height / 2 + 200)
        # draw_text("Home", small_font, (255, 255, 255), main_screen, 90, 50)
        # draw_text("Quit", small_font, (255, 255, 255), main_screen, 1190, 50)

        click = False  # resets the mouse click

        # checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        # updates the game and tick
        pygame.display.update()
        clock.tick(60)


def betting_screen():
    """---------------------------------SETUP-------------------------------"""
    click = False  # resets the mouse click to avoid a bug where one click would trigger two events

    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse

    smallbet_button = pygame.Rect((screen_width // 2) - 500, (screen_height // 2) + 60, 200, 80)
    medbet_button = pygame.Rect((screen_width // 2) - 100, (screen_height // 2) + 60, 200, 80)
    bigbet_button = pygame.Rect((screen_width // 2) + 300, (screen_height // 2) + 60, 200, 80)

    """"----------------------------------LOOP-------------------------------"""

    while True:  # screen loop
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        # Check for mouse over and mouse click on the easy button, button changes color on mouse over
        if smallbet_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), smallbet_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()

        else:
            pygame.draw.rect(main_screen, (196, 16, 16), smallbet_button, 0, 5)

        if medbet_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), medbet_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()

        else:
            pygame.draw.rect(main_screen, (196, 16, 16), medbet_button, 0, 5)

        if bigbet_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), bigbet_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()

        else:
            pygame.draw.rect(main_screen, (196, 16, 16), bigbet_button, 0, 5)

        draw_text("Bet Small", small_font, (255, 255, 255), main_screen, (screen_width // 2) - 410,
                  screen_height / 2 + 100)
        draw_text("Bet Medium", small_font, (255, 255, 255), main_screen, (screen_width // 2) ,
                  screen_height / 2 + 100)
        draw_text("Bet Big", small_font, (255, 255, 255), main_screen, (screen_width // 2) + 400, screen_height / 2 + 100)

        click = False  # resets the mouse click

        # Checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        # updates the game and tick
        pygame.display.update()
        clock.tick(60)


def tutorials(tutorial):
    click = False  # resets the mouse click to avoid a bug where one click would trigger two events

    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse
    return_button = pygame.Rect((screen_width // 2) + 500, (screen_height // 2) -300, 100, 100)

    while True:
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        # Checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()

        draw_text(tutorial, big_font, (255, 255, 255), main_screen, screen_width // 2, screen_height / 2 - 170)

        click = False  # resets the mouse click

        # Checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        # updates the game and tick
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    menu(mouse_click, "Fraction Distraction")
