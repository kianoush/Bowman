__author__ = 'kian'
import pygame
pygame.init()

Display_height = 1000
Display_wight = 800

Display = pygame.display.set_mode((Display_height,Display_wight))
pygame.display.set_caption('kian')

walk_Img = [pygame.image.load('2_WALK_000.png'),pygame.image.load('2_WALK_001.png'),pygame.image.load('2_WALK_002.png')\
    ,pygame.image.load('2_WALK_003.png'),pygame.image.load('2_WALK_004.png')]

jump_Img = [pygame.image.load('4_JUMP_000.png'),pygame.image.load('4_JUMP_001.png'),pygame.image.load('4_JUMP_002.png')\
    ,pygame.image.load('4_JUMP_003.png'),pygame.image.load('4_JUMP_004.png')]

attack = [pygame.image.load('5_ATTACK_000.png'),pygame.image.load('5_ATTACK_003.png'),pygame.image.load('5_ATTACK_005.png')\
    ,pygame.image.load('5_ATTACK_007.png'),pygame.image.load('5_ATTACK_009.png')]

monster_walk=[pygame.image.load('RUN_0000.png'),pygame.image.load('RUN_0001.png'),pygame.image.load('RUN_0002.png'),\
    pygame.image.load('RUN_0003.png'),pygame.image.load('RUN_0004.png'),pygame.image.load('RUN_0005.png'),pygame.image.load('RUN_0006.png')]

monster_die=[pygame.image.load('DIE_0001.png'),pygame.image.load('DIE_0002.png')\
    ,pygame.image.load('DIE_0003.png'),pygame.image.load('DIE_0004.png'),pygame.image.load('DIE_0005.png'),pygame.image.load('DIE_0006.png')]

bg = pygame.image.load('1.png')
standing = pygame.image.load('6_HURT_000.png')
dart1 = pygame.image.load('dart.png')


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

    def man_walk(self,Display):
        #global walkCount
        #global jump_jump

        if self.walkCount + 1 >= 21 or self.jump_jump + 1 >= 21 or self.attackCount + 1 >= 6 :
            self.walkCount = 0
            self.jump_jump = 0
            self.attackCount = 0
        if self.right:
            Display.blit(walk_Img[self.walkCount//4],(self.x,self.y))
            #print ('w:',self.walkCount//5)
            self.walkCount += 1
        elif self.left:
            Display.blit(walk_Img[-(self.walkCount-19)//4],(self.x,self.y))
            #print(-(self.walkCount-19)//4)
            self.walkCount += 1
        elif self.jump:
            Display.blit(jump_Img[self.jump_jump//4],(self.x,self.y))
            self.jump_jump += 1
        elif self.attack:
            Display.blit(attack[(self.attackCount)],(self.x,self.y))
            #print('A:',(self.attackCount//4))
            self.attackCount += 1
        else:
            Display.blit(standing,(self.x,self.y))

        self.hitbox = (self.x + 15, self.y + 5, 60, 80)
        pygame.draw.rect(Display, (255,0,0), self.hitbox,2)



        pygame.display.update()



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
            Display.blit(dart1,(self.x ,self.y))
            print('Attack:', self.x )
            self.dartCount += 1
        pygame.display.update()


class mon(object):
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
            #self.live = False
        if self.live:
            Display.blit(monster_walk[self.monsterwalkCount//2],(self.x,self.y))
            #print ('mon:',self.monsterwalkCount//3)
            self.monsterwalkCount += 1
            self.x -= self.move
            pygame.display.update()
        if self.dead:
            monster.live = False
            Display.blit(monster_die[self.monsterwalkCount1//4],(self.x,self.y))
            #print ('mon:',self.monsterwalkCount//3)
            self.monsterwalkCount1 += 1
            pygame.display.update()
        self.hitbox = (self.x+25 , self.y-5 , 140, 120)
        pygame.draw.rect(Display, (255,0,0), self.hitbox,2)

def combat_walk():
    Display.blit(bg,(0,0))
    dart_Man.attack_dart(Display)
    combat.man_walk(Display)
    pygame.display.update()
    #monster.monster_draw(Display)

combat = player(100,505,60,60)
dart_Man = dart(combat.x,combat.y)
monster = mon(700,482)
run = True

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] :
        combat.x -= combat.move
        combat.right = False
        combat.left = True

    elif keys[pygame.K_RIGHT]:
        combat.x += combat.move
        combat.right = True
        combat.left = False

    elif keys[pygame.K_SPACE]:
        combat.attack = True
        dart_Man.attack = True
        #dart_Man.x = combat.x
        dart_Man.x += dart_Man.move
        if dart_Man.x > 1000:
                dart_Man.x = combat.x
        if dart_Man.x > monster.x :
            dart_Man.x = combat.x
            dart_Man.shoot += 1
            if dart_Man.shoot >= 4:
                dart_Man.shoot = 0
                #monster.live = False
                monster.dead = True
                #monster.monstar_Dead()
        pygame.display.update()


    else:
        #standing
        combat.attack = False
        combat.right = False
        combat.left = False
        dart_Man.attack = False
        combat.walkCount = 0
        combat.attackCount = 0
    if not (combat.jump):
        if keys[pygame.K_UP]:
            combat.jump = True
            combat.right = False
            combat.left = False
            combat.walkCount = 0
            combat.attackCount = 0
    else:
        #print(combat.jumpCount)
        if combat.jumpCount >= -8:
            k = 1
            if combat.jumpCount < 0:
                k = -1
            combat.y -= (combat.jumpCount ** 2) * 0.5 * k
            combat.jumpCount -= 1
        else:
            combat.jump = False
            combat.jumpCount = 8
    #pygame.draw.rect(Display,(255,0,0),(x,y,height,width))
    #pygame.display.update()
    Display.blit(dart1,(dart_Man.x ,dart_Man.y))
    dart_Man.x += dart_Man.move
    combat_walk()
    monster.monster_draw(Display)
    #print(dartman.x , monster.x)
    pygame.display.update()


pygame.quit()
quit()



