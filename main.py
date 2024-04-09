import pygame
import random
import os

pygame.init()


# CONSTANTES GLOBALES

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CaPYbara Run")

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

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

class Capybara:
    X_POS = 80
    Y_POS = 311
    Y_POS_DUCK = 350
    JUMP_VEL = 8.5 
    
    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        
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
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
        
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

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
        self.rect.y = 325
        
        
class LargeBox(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

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
        self.rect.x = SCREEN_WIDTH * 1.5

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
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, fruits
    run = True
    clock = pygame.time.Clock()
    player = Capybara()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    fruits = []
    death_count = 0
    
    def score():
        global points, game_speed
        if points % 30 == 0 and points > 0:
            game_speed += 1
        text = font.render("Puntos: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)
    
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed
        
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # SCREEN.fill((255, 255 ,255))
        SCREEN.fill((111, 176, 183))
        userInput = pygame.key.get_pressed()
        
        player.draw(SCREEN)
        player.update(userInput)
        
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallBox(SMALL_BOX))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeBox(LARGE_BOX))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))
                
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.capy_rect.colliderect(obstacle.rect):
                # pygame.draw.rect(SCREEN, (255, 0, 0), player.capy_rect, 2) #mostrar hitbox cuando choca con obstaculo
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
                
        if len(fruits) == 0:
            if random.randint(0, 1) == 0:
                fruits.append(Cherry(FRUITS))
            elif random.randint(0, 1) == 1:
                fruits.append(Watermelon(FRUITS))
        
        for fruit in fruits:
            fruit.draw(SCREEN)
            fruit.update()
            if player.capy_rect.colliderect(fruit.rect):
                fruits.pop()
                points += 1
        
        cloud.draw(SCREEN)
        cloud.update()
        
        background()
        
        score()
        
        clock.tick(30)
        pygame.display.update()



def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((111, 176, 183))
        font = pygame.font.Font('freesansbold.ttf', 20)
        
        if death_count == 0:
            text = font.render ("Presiona cualquier tecla para empezar ", True, (0, 0, 0))
            controls = font.render ("Controles: Flecha arriba para saltar, flecha abajo para agacharse" , True, (0, 0, 0))
            controlsRect = controls.get_rect()
            controlsRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(controls, controlsRect)

        elif death_count > 0:
            text = font.render ("Presiona cualquier tecla para volver a empezar", True, (0, 0, 0))
            score = font.render("Tus puntos: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)