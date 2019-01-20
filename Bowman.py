
import pygame
pygame.init()

Display_height = 1000
Display_wight = 800

# Load bowman images 

Display = pygame.display.set_mode((Display_height,Display_wight))
pygame.display.set_caption('Bowman')

walk_Img = [pygame.image.load('2_WALK_000.png'),pygame.image.load('2_WALK_001.png'),pygame.image.load('2_WALK_002.png')\
    ,pygame.image.load('2_WALK_003.png'),pygame.image.load('2_WALK_004.png')]

jump_Img = [pygame.image.load('4_JUMP_000.png'),pygame.image.load('4_JUMP_001.png'),pygame.image.load('4_JUMP_002.png')\
    ,pygame.image.load('4_JUMP_003.png'),pygame.image.load('4_JUMP_004.png')]

attack_Img = [pygame.image.load('5_ATTACK_000.png'),pygame.image.load('5_ATTACK_003.png'),pygame.image.load('5_ATTACK_005.png')\
    ,pygame.image.load('5_ATTACK_007.png'),pygame.image.load('5_ATTACK_009.png')]

bg_Img = pygame.image.load('1.png')
standing_Img = pygame.image.load('6_HURT_000.png')
dart1_Img = pygame.image.load('dart.png')

# Make a class for player
clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.move = 15
        self.walkCount = 0
        self.jumpCount = 8
        self.jump_jump = 0
        self.attackCount = 0
        self.dartCount = 0
        self.right = False
        self.left = False
        self.jump = False
        self.standing = False
        self.attack = False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def Bowman_walk(self,Display):

        if self.walkCount + 1 >= 21 or self.jump_jump + 1 >= 21 or self.attackCount + 1 >= 6 :
            self.walkCount = 0
            self.jump_jump = 0
            self.attackCount = 0
        if self.right:
            Display.blit(walk_Img[self.walkCount//4],(self.x,self.y))
            self.walkCount += 1
        elif self.left:
            Display.blit(walk_Img[-(self.walkCount-19)//4],(self.x,self.y))
            self.walkCount += 1
        elif self.jump:
            Display.blit(jump_Img[self.jump_jump//4],(self.x,self.y))
            self.jump_jump += 1
        elif self.attack:
            Display.blit(attack_Img[(self.attackCount)],(self.x,self.y))
            self.attackCount += 1
        else:
            Display.blit(standing_Img,(self.x,self.y))

        self.hitbox = (self.x + 15, self.y + 5, 60, 80)
        #pygame.draw.rect(Display, (255,0,0), self.hitbox,2)

        pygame.display.update()

# Make a class for dart

class dart(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.move = 50
        self.attack = False
        self.dartCount = 0
        self.shoot = 0

    def attack_dart(self,Display):
        if self.attack:
            Display.blit(dart1_Img,(self.x ,self.y))
            print('Attack:', self.x )
            self.dartCount += 1
        pygame.display.update()

# Load Images for monster
monster_walk_Img=[pygame.image.load('RUN_0000.png'),pygame.image.load('RUN_0001.png'),pygame.image.load('RUN_0002.png'),\
    pygame.image.load('RUN_0003.png'),pygame.image.load('RUN_0004.png'),pygame.image.load('RUN_0005.png'),pygame.image.load('RUN_0006.png')]

monster_die_Img=[pygame.image.load('DIE_0001.png'),pygame.image.load('DIE_0002.png')\
    ,pygame.image.load('DIE_0003.png'),pygame.image.load('DIE_0004.png'),pygame.image.load('DIE_0005.png'),pygame.image.load('DIE_0006.png')]

#Make a class for monster

class monster(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.monsterwalkCount = 0
        self.monsterwalkCount1 = 0
        self.move = 1
        self.live = True
        self.dead = False
        self.hitbox = (self.x , self.y , 29, 52)

    def monster_draw(self,Display):
        if self.monsterwalkCount + 1 >= 14 or self.monsterwalkCount1 + 1 >= 24:
            self.monsterwalkCount = 0
            self.monsterwalkCount1 = 0
            self.dead = False
        if self.live:
            Display.blit(monster_walk_Img[self.monsterwalkCount//2],(self.x,self.y))
            self.monsterwalkCount += 1
            self.x -= self.move
            pygame.display.update()
        if self.dead:
            self.live = False
            Display.blit(monster_die_Img[self.monsterwalkCount1//4],(self.x,self.y))
            self.monsterwalkCount1 += 1
            pygame.display.update()
        self.hitbox = (self.x+25 , self.y-5 , 140, 120)
        #pygame.draw.rect(Display, (255,0,0), self.hitbox,2)
#Draw all classes
def Bowman_walk_Draw():
    Display.blit(bg_Img,(0,0))
    dart_Man.attack_dart(Display)
    Bowman.Bowman_walk(Display)
    pygame.display.update()

# Main loop   
Bowman = player(100,505,60,60)
dart_Man = dart(Bowman.x,Bowman.y+20)
monster_01 = monster(700,482)

run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] :
        Bowman.x -= Bowman.move
        Bowman.right = False
        Bowman.left = True

    elif keys[pygame.K_RIGHT]:
        Bowman.x += Bowman.move
        Bowman.right = True
        Bowman.left = False

    elif keys[pygame.K_SPACE]:
        Bowman.attack = True
        dart_Man.attack = True
        dart_Man.x += dart_Man.move
        if dart_Man.x > 1000:
                dart_Man.x = Bowman.x
        if dart_Man.x > monster_01.x :
            dart_Man.x = Bowman.x
            dart_Man.shoot += 1
            if dart_Man.shoot >= 4:
                dart_Man.shoot = 0
                monster_01.dead = True
        pygame.display.update()
    else:
        #player standing 
        Bowman.attack = False
        Bowman.right = False
        Bowman.left = False
        dart_Man.attack = False
        Bowman.walkCount = 0
        Bowman.attackCount = 0
    if not (Bowman.jump):
        if keys[pygame.K_UP]:
            Bowman.jump = True
            Bowman.right = False
            Bowman.left = False
            Bowman.walkCount = 0
            Bowman.attackCount = 0
    else:
        if Bowman.jumpCount >= -8:
            k = 1
            if Bowman.jumpCount < 0:
                k = -1
            Bowman.y -= (Bowman.jumpCount ** 2) * 0.5 * k
            Bowman.jumpCount -= 1
        else:
            Bowman.jump = False
            Bowman.jumpCount = 8

    Display.blit(dart1_Img,(dart_Man.x ,dart_Man.y))
    dart_Man.x += dart_Man.move
    Bowman_walk_Draw()
    monster_01.monster_draw(Display)
    pygame.display.update()


pygame.quit()
quit()



