import pygame, os

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CaPYbara Run")
ICON = pygame.image.load(os.path.join("src", "capybara.png"))
pygame.display.set_icon(ICON)



RUNNING = [
        pygame.image.load(os.path.join("Assets/Capy", "CapyRun0.png")),
        pygame.image.load(os.path.join("Assets/Capy", "CapyRun1.png")),
        pygame.image.load(os.path.join("Assets/Capy", "CapyRun2.png")),
        pygame.image.load(os.path.join("Assets/Capy", "CapyRun3.png")),
        pygame.image.load(os.path.join("Assets/Capy", "CapyRun4.png"))
        ]
JUMPING = pygame.image.load(os.path.join("Assets/Capy", "CapyJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Capy", "CapyDuck1.png")),
        pygame.image.load(os.path.join("Assets/Capy", "CapyDuck2.png"))]




SMALL_BOX = [pygame.image.load(os.path.join("Assets/Box", "SmallBox1.png")),
                pygame.image.load(os.path.join("Assets/Box", "SmallBox2.png")),
                pygame.image.load(os.path.join("Assets/Box", "SmallBox3.png"))]
LARGE_BOX = [pygame.image.load(os.path.join("Assets/Box", "LargeBox1.png")),
                pygame.image.load(os.path.join("Assets/Box", "LargeBox2.png")),
                pygame.image.load(os.path.join("Assets/Box", "LargeBox3.png"))]
FRUITS = [pygame.image.load(os.path.join("Assets/Fruits", "Cherry.png")),
        pygame.image.load(os.path.join("Assets/Fruits", "Watermelon.png"))]
BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
TRACK = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
FONT = os.path.join("Assets/Font", "PressStart2P-Regular.ttf")

MENU_BACKGROUND = pygame.image.load(os.path.join("Assets/GUI", "Background.png"))


PLAY_BUTTON = pygame.image.load(os.path.join("Assets/GUI", "Play Rect.png"))
OPTIONS_BUTTON = pygame.image.load(os.path.join("Assets/GUI", "Options Rect.png"))
QUIT_BUTTON = pygame.image.load(os.path.join("Assets/GUI", "Quit Rect.png"))