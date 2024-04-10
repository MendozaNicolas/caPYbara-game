from button import Button
import pygame, sys, os
import globals
import random

pygame.init()



SOUNDS_FRUIT = pygame.mixer.Sound(os.path.join("Assets/Sounds", "fruit.wav"))
SOUNDS_JUMP = pygame.mixer.Sound(os.path.join("Assets/Sounds", "jump.wav"))
SOUNDS_OPTION = pygame.mixer.Sound(os.path.join("Assets/Sounds", "option.wav"))
SOUNDS_DEATH = pygame.mixer.Sound(os.path.join("Assets/Sounds", "death.wav"))


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(globals.FONT, size)

# Clases

class Capybara:
    X_POS = 80
    Y_POS = 311
    Y_POS_DUCK = 350
    JUMP_VEL = 8.5 
    
    def __init__(self):
        self.duck_img = globals.DUCKING
        self.run_img = globals.RUNNING
        self.jump_img = globals.JUMPING
        
        self.capy_duck = False
        self.capy_run = True
        self.capy_jump = False
        
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.capy_rect = self.image.get_rect()
        self.capy_rect.x = self.X_POS
        self.capy_rect.y = self.Y_POS
        
    def update(self, userInput):
        if self.capy_duck:
            self.duck()
        if self.capy_run:
            self.run()
        if self.capy_jump:
            self.jump()
            
        if self.step_index >= 10:
            self.step_index = 0
            
        if userInput[pygame.K_UP] and not self.capy_jump:
            self.capy_duck = False
            self.capy_run = False
            self.capy_jump = True
        elif userInput[pygame.K_DOWN] and not self.capy_jump:
            self.capy_duck = True
            self.capy_run = False
            self.capy_jump = False
        elif not (self.capy_jump or userInput[pygame.K_DOWN]):
            self.capy_duck = False
            self.capy_run = True
            self.capy_jump = False
            
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.capy_rect = self.image.get_rect()
        self.capy_rect.x = self.X_POS
        self.capy_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.capy_rect = self.image.get_rect()
        self.capy_rect.x = self.X_POS
        self.capy_rect.y = self.Y_POS
        self.step_index += 1
    
    def jump(self):
        self.image = self.jump_img
        if self.jump_vel == self.JUMP_VEL:
            SOUNDS_JUMP.play()
        if self.capy_jump:
            self.capy_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.capy_jump = False
            self.jump_vel = self.JUMP_VEL
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.capy_rect.x, self.capy_rect.y))

class Cloud:
    def __init__(self):
        self.x = globals.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = globals.CLOUD
        self.width = self.image.get_width()
        
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = globals.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = globals.SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallBox(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 358.5
        
        
class LargeBox(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 350

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0
        
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class Fruit:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = globals.SCREEN_WIDTH * 1.5

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            fruits.pop()
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)
        

class Cherry(Fruit):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 315
        
class Watermelon(Fruit):
    def __init__(self, image):
        self.type = 1
        super().__init__(image, self.type)
        self.rect.y = 315


    

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, fruits, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Capybara()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font(globals.FONT, 24)
    obstacles = []
    fruits = []
    death_count = 0
    
    
    
    def score():
        global points, game_speed
        if points % 30 == 0 and points > 0:
            game_speed += 1
        text = font.render("Puntos: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (950, 40)
        globals.SCREEN.blit(text, textRect)
    
    def background():
        global x_pos_bg, y_pos_bg
        image_width = globals.TRACK.get_width()
        globals.SCREEN.blit(globals.TRACK, (x_pos_bg, y_pos_bg))
        globals.SCREEN.blit(globals.TRACK, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            globals.SCREEN.blit(globals.TRACK, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed
        
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # SCREEN.fill((255, 255 ,255))
        globals.SCREEN.fill((111, 176, 183))
        userInput = pygame.key.get_pressed()
        
        player.draw(globals.SCREEN)
        player.update(userInput)
        
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallBox(globals.SMALL_BOX))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeBox(globals.LARGE_BOX))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(globals.BIRD))
                
        for obstacle in obstacles:
            obstacle.draw(globals.SCREEN)
            obstacle.update()
            if player.capy_rect.colliderect(obstacle.rect):
                # pygame.draw.rect(SCREEN, (255, 0, 0), player.capy_rect, 2) #mostrar hitbox cuando choca con obstaculo
                SOUNDS_DEATH.play()
                pygame.time.delay(2000)
                death_count += 1
                gameover(death_count)
                
        if len(fruits) == 0:
            if random.randint(0, 1) == 0:
                fruits.append(Cherry(globals.FRUITS))
            elif random.randint(0, 1) == 1:
                fruits.append(Watermelon(globals.FRUITS))
        
        for fruit in fruits:
            fruit.draw(globals.SCREEN)
            fruit.update()
            if player.capy_rect.colliderect(fruit.rect):
                fruits.pop()
                SOUNDS_FRUIT.play()
                points += 1
        
        cloud.draw(globals.SCREEN)
        cloud.update()
        
        background()
        
        score()
        
        clock.tick(30)
        pygame.display.update()


def gameover(death_count):
    global points
    run = True
    
    while run:
        globals.SCREEN.fill((111, 176, 183))
        font = pygame.font.Font(globals.FONT, 24)
        
        

        if death_count == 0:
            main_menu()

        elif death_count > 0:
            text = font.render("Presiona cualquier tecla para volver a empezar", True, (0, 0, 0))
            score = font.render("Tus puntos: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (globals.SCREEN_WIDTH // 2, globals.SCREEN_HEIGHT // 2 + 50)
            globals.SCREEN.blit(score, scoreRect)
            textRect = text.get_rect()
            textRect.center = (globals.SCREEN_WIDTH // 2, globals.SCREEN_HEIGHT // 2)
            globals.SCREEN.blit(text, textRect)
        # globals.SCREEN.blit(globals.RUNNING[0], (globals.SCREEN_WIDTH // 2 - 20, globals.SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                main()



def play():
    main()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        globals.SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        globals.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(globals.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        globals.SCREEN.blit(globals.MENU_BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("CAPYBARA", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(globals.SCREEN_WIDTH // 2, globals.SCREEN_HEIGHT // 2 - 220))

        PLAY_BUTTON = Button(None, pos=(globals.SCREEN_WIDTH // 2, globals.SCREEN_HEIGHT// 2 - 50), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(None, pos=(globals.SCREEN_WIDTH // 2, globals.SCREEN_HEIGHT // 2 + 75), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(None, pos=(globals.SCREEN_WIDTH // 2, globals.SCREEN_HEIGHT // 2 + 200), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        globals.SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(globals.SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    SOUNDS_OPTION.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    SOUNDS_OPTION.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    SOUNDS_OPTION.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# 
gameover(death_count=0)