from classes import Player, Yintercept
import pygame
import sys
from fractions import Fraction
import random
import time

# initializes the game and pygame fonts
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Fraction Distraction")

# initializes game sound effects
button_sound = pygame.mixer.Sound("Assets/button.mp3")
error_sound = pygame.mixer.Sound("Assets/error.mp3")

# basic global values
screen_width = 1280
screen_height = 720
mouse_click = False

# creates the main screen of the game
main_screen = pygame.display.set_mode((screen_width, screen_height))

# loads in the assets (background, fonts, and assets)
start_background = pygame.image.load("Assets/start_bg.jpg")
big_font = pygame.font.Font("Assets/zx_spectrum.ttf", 50)

money = pygame.image.load("Assets/money.png")
money = pygame.transform.scale(money, (89, 80))
money_rect = money.get_rect()
money_rect.center = (1250, 675)

heart = pygame.image.load("Assets/heart.png")
heart = pygame.transform.scale(heart, (54, 45))
heart_rect = heart.get_rect()
heart_rect.center = (screen_width / 2 + 300, 680)

medium_font = pygame.font.Font("Assets/zx_spectrum.ttf", 35)
small_font = pygame.font.Font("Assets/zx_spectrum.ttf", 25)


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


def draw_text_outline(text, font, color, surface, x, y):
    """ utilizes draw_text to create a black outline

    :param text: string of the text
    :param font: font of the text, should be in the .ttf file format
    :param color: color of the text, can be in r,g,b or string: https://www.discogcodingacademy.com/turtle-colours
    :param surface: the screen that the text will be on
    :param x: x-position of the text - middle of the text box
    :param y: y-position of the text - middle of the text bos
    """

    if font == small_font:
        draw_text(text, font, color, surface, x, y)
    else:
        black_color = (0, 0, 0)

        # Draws the black outline
        draw_text(text, font, black_color, surface, x - 2, y - 2)
        draw_text(text, font, black_color, surface, x - 2, y + 2)
        draw_text(text, font, black_color, surface, x + 2, y - 2)
        draw_text(text, font, black_color, surface, x + 2, y + 2)

        # Draws the real text against black background text
        draw_text(text, font, color, surface, x, y)


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

    draw_text_outline("Home", small_font, (255, 255, 255), main_screen, 90, 50)
    draw_text_outline("Quit", small_font, (255, 255, 255), main_screen, 1190, 50)


def money_UI():
    """ creates the UI for the total money the player has"""

    main_screen.blit(money, money_rect)
    draw_text_outline(f"${player.total_money}", medium_font, (255, 255, 255), main_screen, 1160, 680)


def item_UI():
    """ creates the UI for the amount of items the player has"""

    draw_text_outline(f"X2: {player.items['double_bet']}", medium_font, (255, 255, 255), main_screen,
                      screen_width / 2 - 300, 680)
    draw_text_outline(f"X3: {player.items['triple_bet']}", medium_font, (255, 255, 255), main_screen,
                      screen_width / 2, 680)
    main_screen.blit(heart, heart_rect)
    draw_text_outline(f": {player.items['life_line']}", medium_font, (255, 255, 255), main_screen,
                      screen_width / 2 + 360, 680)


def answer_choice_text(correct_option, answer, fake_1, fake_2):
    """generates the random answer choices

    :param correct_option: the correct option, 1 = left, 2 = middle, 3= right
    :param answer: the correct answer fraction
    :param fake_1: fake answer fraction
    :param fake_2: fake answer fraction
    """

    if correct_option == 1:
        draw_text_outline(f"{answer}", medium_font, (255, 255, 255), main_screen, (screen_width // 2) - 400,
                          screen_height // 2 + 240)  # answer 1
        draw_text_outline(f"{fake_1}", medium_font, (255, 255, 255), main_screen, (screen_width // 2),
                          screen_height // 2 + 240)  # answer 2
        draw_text_outline(f"{fake_2}", medium_font, (255, 255, 255), main_screen, (screen_width // 2) + 400,
                          screen_height // 2 + 240)  # answer 3
    elif correct_option == 2:
        draw_text_outline(f"{fake_1}", medium_font, (255, 255, 255), main_screen, (screen_width // 2) - 400,
                          screen_height // 2 + 240)  # answer 1
        draw_text_outline(f"{answer}", medium_font, (255, 255, 255), main_screen, (screen_width // 2),
                          screen_height // 2 + 240)  # answer 2
        draw_text_outline(f"{fake_2}", medium_font, (255, 255, 255), main_screen, (screen_width // 2) + 400,
                          screen_height // 2 + 240)  # answer 3
    else:
        draw_text_outline(f"{fake_1}", medium_font, (255, 255, 255), main_screen, (screen_width // 2) - 400,
                          screen_height // 2 + 240)  # answer 1
        draw_text_outline(f"{fake_2}", medium_font, (255, 255, 255), main_screen, (screen_width // 2),
                          screen_height // 2 + 240)  # answer 2
        draw_text_outline(f"{answer}", medium_font, (255, 255, 255), main_screen, (screen_width // 2) + 400,
                          screen_height // 2 + 240)  # answer 3


def tutorial_steps(tutorial):
    steps = []
    if tutorial == 'Find Y-intercept Form':
        tut = Yintercept(['6x', '7y', '9'])
        steps.append(tut.equation)
        return steps


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
                sys.exit()
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), quit_button, 0, 5)

        # Check for mouse over and mouse click on the quit button, button changes color on mouse over
        if shop_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), shop_button, 0, 5)
            if click:
                button_sound.play()
                shop_screen()
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), shop_button, 0, 5)

        # Draws text on the menu screen
        draw_text_outline(message, big_font, (255, 255, 255), main_screen, screen_width / 2, screen_height / 2 - 170)
        draw_text_outline("Shop", medium_font, (255, 255, 255), main_screen, screen_width / 2 + 230,
                          screen_height / 2 - 40)
        draw_text_outline("Betting", medium_font, (255, 255, 255), main_screen, screen_width / 2 - 230,
                          screen_height / 2 - 40)
        draw_text_outline("Quit", medium_font, (255, 255, 255), main_screen, screen_width / 2 + 230,
                          screen_height / 2 + 80)
        draw_text_outline("Tutorial", medium_font, (255, 255, 255), main_screen, screen_width / 2 - 230,
                          screen_height / 2 + 80)

        item_UI()
        money_UI()

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
                tutorials('Adding/Subtracting Fractions')
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), add_button, 0, 5)

        # Check for mouse over and mouse click on the hard button, button changes color on mouse over
        if multiply_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), multiply_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Multiplying/Dividing Fractions')

        else:
            pygame.draw.rect(main_screen, (196, 16, 16), multiply_button, 0, 5)

        # Check for mouse over and mouse click on the 2-player button, button changes color on mouse over
        if lcd_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), lcd_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Find Least Common Demoniator')
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), lcd_button, 0, 5)

        if y_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), y_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Transform Fraction')
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), y_button, 0, 5)

        if transform_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), transform_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Find Y-intercept Form')

        else:
            pygame.draw.rect(main_screen, (196, 16, 16), transform_button, 0, 5)

        # Draws text on the tutorial menu screen
        draw_text_outline(message, big_font, (255, 255, 255), main_screen, screen_width // 2, screen_height / 2 - 170)
        draw_text_outline("Add/Subtract", small_font, (255, 255, 255), main_screen, (screen_width // 2) - 270,
                          screen_height / 2 - 40)
        draw_text_outline("Multiply/Divide", small_font, (255, 255, 255), main_screen, (screen_width // 2) + 270,
                          screen_height / 2 - 40)
        draw_text_outline("LCD", small_font, (255, 255, 255), main_screen, screen_width // 2, screen_height / 2 + 80)
        draw_text_outline("Transform Fraction", small_font, (255, 255, 255), main_screen, (screen_width // 2) + 270,
                          screen_height / 2 + 200)
        draw_text_outline("Y-Intercept Form", small_font, (255, 255, 255), main_screen, (screen_width // 2) - 270,
                          screen_height / 2 + 200)
        # draw_text_outline()("Home", small_font, (255, 255, 255), main_screen, 90, 50)
        # draw_text_outline()("Quit", small_font, (255, 255, 255), main_screen, 1190, 50)

        money_UI()

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

    table = pygame.image.load("Assets/table.png")
    table = pygame.transform.scale(table, (765, 464))
    table_rec = table.get_rect()
    table_rec.center = (640, 200)

    smallbet_button = pygame.Rect((screen_width // 2) - 500, (screen_height // 2) + 60, 200, 80)
    medbet_button = pygame.Rect((screen_width // 2) - 100, (screen_height // 2) + 60, 200, 80)
    bigbet_button = pygame.Rect((screen_width // 2) + 300, (screen_height // 2) + 60, 200, 80)
    home_button = pygame.Rect(30, 20, 120, 60)
    quit_button = pygame.Rect(1130, 20, 120, 60)

    """"----------------------------------LOOP-------------------------------"""

    while True:  # screen loop
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        universal_UI(home_button, quit_button, mx, my, click)

        # Check for mouse over and mouse click on the easy button, button changes color on mouse over
        if smallbet_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), smallbet_button, 0, 5)
            if click:
                button_sound.play()
                wager_screen("small")
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), smallbet_button, 0, 5)

        if medbet_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), medbet_button, 0, 5)
            if click:
                button_sound.play()
                wager_screen("med")
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), medbet_button, 0, 5)

        if bigbet_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), bigbet_button, 0, 5)
            if click:
                button_sound.play()
                wager_screen("big")
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), bigbet_button, 0, 5)

        draw_text_outline("Bet Small", small_font, (255, 255, 255), main_screen, (screen_width // 2) - 400,
                          screen_height / 2 + 100)
        draw_text_outline("Bet Med", small_font, (255, 255, 255), main_screen, (screen_width // 2),
                          screen_height / 2 + 100)
        draw_text_outline("Bet Big", small_font, (255, 255, 255), main_screen, (screen_width // 2) + 400,
                          screen_height / 2 + 100)

        item_UI()
        money_UI()

        click = False  # resets the mouse click

        # Checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        main_screen.blit(table, table_rec)

        # updates the game and tick
        pygame.display.update()
        clock.tick(60)


def wager_screen(mode):
    """---------------------------------SETUP-------------------------------"""

    click = False  # resets the mouse click to avoid a bug where one click would trigger two events

    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse

    table = pygame.image.load("Assets/table.png")
    table = pygame.transform.scale(table, (765, 464))
    table_rec = table.get_rect()
    table_rec.center = (640, 200)

    wager1_button = pygame.Rect((screen_width // 2) - 500, (screen_height // 2) + 60, 200, 80)
    wager2_button = pygame.Rect((screen_width // 2) - 100, (screen_height // 2) + 60, 200, 80)
    wager3_button = pygame.Rect((screen_width // 2) + 300, (screen_height // 2) + 60, 200, 80)
    home_button = pygame.Rect(30, 20, 120, 60)
    quit_button = pygame.Rect(1130, 20, 120, 60)

    """"----------------------------------LOOP-------------------------------"""

    while True:  # screen loop
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        universal_UI(home_button, quit_button, mx, my, click)

        # Check for mouse over and mouse click on the easy button, button changes color on mouse over
        if wager1_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), wager1_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                player.bet(15)
                betting_game_screen(mode)
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), wager1_button, 0, 5)

        if wager2_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), wager2_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                player.bet(25)
                betting_game_screen(mode)
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), wager2_button, 0, 5)

        if wager3_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), wager3_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                player.bet(50)
                betting_game_screen(mode)
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), wager3_button, 0, 5)

        draw_text_outline("$15", small_font, (255, 255, 255), main_screen, (screen_width // 2) - 400,
                          screen_height / 2 + 100)
        draw_text_outline("$25", small_font, (255, 255, 255), main_screen, (screen_width // 2),
                          screen_height / 2 + 100)
        draw_text_outline("$50", small_font, (255, 255, 255), main_screen, (screen_width // 2) + 400,
                          screen_height / 2 + 100)

        item_UI()
        money_UI()

        click = False  # resets the mouse click

        # Checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        main_screen.blit(table, table_rec)

        # updates the game and tick
        pygame.display.update()
        clock.tick(60)


def betting_game_screen(mode):
    """---------------------------------SETUP-------------------------------"""

    click = False  # resets the mouse click to avoid a bug where one click would trigger two events

    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse

    table = pygame.image.load("Assets/table.png")
    table = pygame.transform.scale(table, (765, 464))
    table_rec = table.get_rect()
    table_rec.center = (640, 200)

    if mode == "small":
        operator = random.randint(0, 1)
        fraction_1 = Fraction(random.randint(1, 20), random.randint(1, 20))
        fraction_2 = Fraction(random.randint(1, 20), random.randint(1, 20))
        if operator == 0:
            answer = fraction_1 * fraction_2
            answer_string = f"{fraction_1} × {fraction_2}"
        else:
            answer = fraction_1 / fraction_2
            answer_string = f"{fraction_1} ÷ {fraction_2}"
    elif mode == "med":
        operator = random.randint(0, 3)
        fraction_1 = Fraction(random.randint(5, 50), random.randint(5, 50))
        fraction_2 = Fraction(random.randint(5, 50), random.randint(5, 50))
        if operator == 0:
            answer = fraction_1 * fraction_2
            answer_string = f"{fraction_1} × {fraction_2}"
        elif operator == 1:
            answer = fraction_1 / fraction_2
            answer_string = f"{fraction_1} ÷ {fraction_2}"
        elif operator == 2:
            answer = fraction_1 + fraction_2
            answer_string = f"{fraction_1} + {fraction_2}"
        else:
            answer = fraction_1 - fraction_2
            answer_string = f"{fraction_1} - {fraction_2}"
    else:
        operator = random.randint(0, 3)
        fraction_1 = Fraction(random.randint(15, 99), random.randint(15, 99))
        fraction_2 = Fraction(random.randint(15, 99), random.randint(15, 99))
        if operator == 0:
            answer = fraction_1 * fraction_2
            answer_string = f"{fraction_1} × {fraction_2}"
        elif operator == 1:
            answer = fraction_1 / fraction_2
            answer_string = f"{fraction_1} ÷ {fraction_2}"
        elif operator == 2:
            answer = fraction_1 + fraction_2
            answer_string = f"{fraction_1} + {fraction_2}"
        else:
            answer = fraction_1 - fraction_2
            answer_string = f"{fraction_1} - {fraction_2}"

    fake_answer_1 = answer * Fraction(random.randint(1, 3), random.randint(2, 3))
    fake_answer_2 = answer * Fraction(random.randint(1, 3), random.randint(2, 3))
    while fake_answer_1 == fake_answer_2 or fake_answer_1 == answer or fake_answer_2 == answer:  # Validates the answers
        fake_answer_1 = answer * Fraction(random.randint(1, 3), random.randint(2, 5))
        fake_answer_2 = answer * Fraction(random.randint(1, 6), random.randint(3, 9))

    correct_answer = random.randint(1, 3)

    # Button recs
    item1_button = pygame.Rect((screen_width // 2) - 500, (screen_height // 2) + 60, 200, 80)
    item2_button = pygame.Rect((screen_width // 2) - 100, (screen_height // 2) + 60, 200, 80)
    item3_button = pygame.Rect((screen_width // 2) + 300, (screen_height // 2) + 60, 200, 80)
    ans1 = pygame.Rect((screen_width // 2) - 550, (screen_height // 2) + 200, 300, 80)
    ans2 = pygame.Rect((screen_width // 2) - 150, (screen_height // 2) + 200, 300, 80)
    ans3 = pygame.Rect((screen_width // 2) + 250, (screen_height // 2) + 200, 300, 80)

    """"----------------------------------LOOP-------------------------------"""

    while True:  # screen loop
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        """Item Buttons"""

        # Check for mouse over and mouse click on the easy button, button changes color on mouse over
        if item1_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), item1_button, 0, 5)
            if click:
                button_sound.play()
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), item1_button, 0, 5)

        if item2_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), item2_button, 0, 5)
            if click:
                button_sound.play()
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), item2_button, 0, 5)

        if item3_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), item3_button, 0, 5)
            if click:
                button_sound.play()
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), item3_button, 0, 5)

        """Answer Buttons"""

        if ans1.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), ans1, 0, 5)
            if click:
                button_sound.play()
                if correct_answer == 1:
                    results(mode, True, answer, answer_string)
                else:
                    results(mode, False, answer, answer_string)
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), ans1, 0, 5)

        if ans2.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), ans2, 0, 5)
            if click:
                button_sound.play()
                if correct_answer == 2:
                    results(mode, True, answer, answer_string)
                else:
                    results(mode, False, answer, answer_string)
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), ans2, 0, 5)

        if ans3.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), ans3, 0, 5)
            if click:
                button_sound.play()
                if correct_answer == 3:
                    results(mode, True, answer, answer_string)
                else:
                    results(mode, False, answer, answer_string)
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), ans3, 0, 5)

        main_screen.blit(table, table_rec)
        draw_text_outline(answer_string, big_font, (255, 255, 255), main_screen, (screen_width // 2), 200)

        draw_text_outline("[ITEM 1]", small_font, (255, 255, 255), main_screen, (screen_width // 2) - 400,
                          screen_height // 2 + 100)
        draw_text_outline("[ITEM 2]", small_font, (255, 255, 255), main_screen, (screen_width // 2),
                          screen_height // 2 + 100)
        draw_text_outline("[ITEM 3]", small_font, (255, 255, 255), main_screen, (screen_width // 2) + 400,
                          screen_height // 2 + 100)

        """Assigning answer to the corresponding options"""

        answer_choice_text(correct_answer, answer, fake_answer_1, fake_answer_2)

        item_UI()
        money_UI()

        click = False  # resets the mouse click

        # Checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.lose()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        # updates the game and tick
        pygame.display.update()
        clock.tick(60)


def results(mode, outcome, answer, question):
    """---------------------------------SETUP-------------------------------"""
    click = False  # resets the mouse click to avoid a bug where one click would trigger two events

    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse

    if outcome:
        money_won = player.win(mode)
    else:
        wage = player.money_on_table
        player.lose()

    table = pygame.image.load("Assets/table.png")
    table = pygame.transform.scale(table, (765, 464))
    table_rec = table.get_rect()
    table_rec.center = (640, 200)

    home_button = pygame.Rect(30, 20, 120, 60)
    quit_button = pygame.Rect(1130, 20, 120, 60)

    """"----------------------------------LOOP-------------------------------"""

    while True:  # screen loop
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        universal_UI(home_button, quit_button, mx, my, click)

        if outcome:
            draw_text_outline(f"Correct! +${money_won}", big_font, (255, 255, 255), main_screen, (screen_width // 2),
                              screen_height / 2 + 100)
        else:
            draw_text_outline(f"Incorrect! -${wage}", big_font, (255, 255, 255), main_screen, (screen_width // 2),
                              screen_height / 2 + 100)
            draw_text_outline(f"Correct Answer: {answer}", big_font, (255, 255, 255), main_screen, (screen_width // 2),
                              screen_height / 2 + 150)

        money_UI()

        click = False  # resets the mouse click

        # Checks for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        main_screen.blit(table, table_rec)
        draw_text_outline(question,
                          big_font, (255, 255, 255), main_screen, (screen_width // 2), 200)

        # updates the game and tick
        pygame.display.update()
        clock.tick(60)


def shop_screen():
    """---------------------------------SETUP-------------------------------"""
    click = False  # resets the mouse click to avoid a bug where one click would trigger two events

    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse

    # Rects for the two buttons
    double_bet_button = pygame.Rect(screen_width / 2 - 420, screen_height / 2 - 80, 370, 80)
    triple_bet_button = pygame.Rect(screen_width / 2 - 420, screen_height / 2 + 20, 370, 80)
    life_line_button = pygame.Rect(screen_width / 2 - 420, screen_height / 2 + 120, 370, 80)
    completed_tutorial_trophy = pygame.Rect(screen_width / 2 + 50, screen_height / 2 - 80, 370, 80)
    earn_money_trophy = pygame.Rect(screen_width / 2 + 50, screen_height / 2 + 20, 370, 80)
    bet_won_trophy = pygame.Rect(screen_width / 2 + 50, screen_height / 2 + 120, 370, 80)
    home_button = pygame.Rect(30, 20, 120, 60)
    quit_button = pygame.Rect(1130, 20, 120, 60)

    """"----------------------------------LOOP-------------------------------"""

    while True:
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        universal_UI(home_button, quit_button, mx, my, click)

        """Items Buttons"""

        if double_bet_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), double_bet_button, 0, 5)
            if click:
                if player.total_money < 10:
                    error_sound.play()
                else:
                    button_sound.play()
                    player.items["double_bet"] += 1
                    player.total_money -= 10
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), double_bet_button, 0, 5)

        if triple_bet_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), triple_bet_button, 0, 5)
            if click:
                if player.total_money < 15:
                    error_sound.play()
                else:
                    button_sound.play()
                    player.items["triple_bet"] += 1
                    player.total_money -= 15
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), triple_bet_button, 0, 5)

        if life_line_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), life_line_button, 0, 5)
            if click:
                if player.total_money < 15:
                    error_sound.play()
                else:
                    button_sound.play()
                    player.items["life_line"] += 1
                    player.total_money -= 30
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), life_line_button, 0, 5)

        """Trophies Buttons"""

        if completed_tutorial_trophy.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), completed_tutorial_trophy, 0, 5)
            if click:
                button_sound.play()
                """Add Tutorial Trophy"""
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), completed_tutorial_trophy, 0, 5)

        if earn_money_trophy.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), earn_money_trophy, 0, 5)
            if click:
                button_sound.play()
                """Add Money Trophy"""
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), earn_money_trophy, 0, 5)

        if bet_won_trophy.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), bet_won_trophy, 0, 5)
            if click:
                button_sound.play()
                "Add Bet Trophy"
        else:
            pygame.draw.rect(main_screen, (196, 16, 16), bet_won_trophy, 0, 5)

        # Draws text on the menu screen
        draw_text_outline("Distracting Shop", big_font, (255, 255, 255), main_screen, screen_width / 2,
                          screen_height / 2 - 170)
        draw_text_outline("Double Bet", medium_font, (255, 255, 255), main_screen, screen_width / 2 - 230,
                          screen_height / 2 - 40)
        draw_text_outline("Triple Bet", medium_font, (255, 255, 255), main_screen, screen_width / 2 - 230,
                          screen_height / 2 + 60)
        draw_text_outline("Life Line", medium_font, (255, 255, 255), main_screen, screen_width / 2 - 230,
                          screen_height / 2 + 160)
        draw_text_outline("Tutorials!", medium_font, (255, 255, 255), main_screen, screen_width / 2 + 230,
                          screen_height / 2 - 40)
        draw_text_outline("Money Won", medium_font, (255, 255, 255), main_screen, screen_width / 2 + 230,
                          screen_height / 2 + 60)
        draw_text_outline("Bets Won", medium_font, (255, 255, 255), main_screen, screen_width / 2 + 230,
                          screen_height / 2 + 160)

        item_UI()
        money_UI()

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


def tutorials(tutorial):
    steps = tutorial_steps(tutorial)
    equation = steps[0]
    click = False  # resets the mouse click to avoid a bug where one click would trigger two events

    pygame.mouse.set_visible(True)  # deals with the visibility of the mouse. allows  user to see and move their mouse
    next_button = pygame.Rect((screen_width // 2) - 100, 600, 200, 100)

    home_button = pygame.Rect(30, 20, 120, 60)
    quit_button = pygame.Rect(1130, 20, 120, 60)

    clicks = []

    while True:
        main_screen.blit(start_background, (0, 0))  # creates the background image

        mx, my = pygame.mouse.get_pos()  # deals with the mouse positions

        universal_UI(home_button, quit_button, mx, my, click)

        if next_button.collidepoint((mx, my)):
            pygame.draw.rect(main_screen, (240, 20, 20), next_button, 0, 5)
            if click:  # calls the main_game function and starts the game
                button_sound.play()
                tutorials('Find Y-intercept Form')
                clicks.append(1)
                print(len(clicks))

        else:
            pygame.draw.rect(main_screen, (196, 16, 16), next_button, 0, 5)

        if len(clicks) == 1:
            print('yes')
        draw_text(tutorial, big_font, (255, 255, 255), main_screen, screen_width // 2, 50)
        draw_text(equation, small_font, (255, 255, 255), main_screen, screen_width // 2, 100)
        draw_text('Next', small_font, (255, 255, 255), main_screen, screen_width//2, 650)

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
    player = Player()
    menu(mouse_click, "Fraction Distraction")
