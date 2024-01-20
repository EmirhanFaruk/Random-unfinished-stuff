
# Modification date: Tue Dec 20 22:35:42 2022

# Production date: Sun Sep  3 15:44:14 2023

import pygame
from random import randint, choice, uniform
from math import sqrt, atan, cos, sin

#Haritaya sınır koy
#Düşmanlar dışarıdan gelsin
#Market/Dalga sistemi
#Değişik silahlar
#Patlayıcılar(?)
#Farklı düşmanlar




ww = 400
wh = 400
win = pygame.display.set_mode((ww, wh))
pygame.init()

eshot = pygame.mixer.Sound("eshot.wav")
pshot = pygame.mixer.Sound("pshot.wav")
pygame.mixer.set_num_channels(10000)

class Human:
    def __init__(self, x, y):
        #props(?)
        self.x = x
        self.y = y
        self.r = 16
        self.vel = 2
        self.maxhp = 100
        self.hp = self.maxhp
        self.alive = True
        self.mr, self.ml, self.mu, self.md = False, False, False, False
        self.milieu = (self.x, self.y)
        self.bulletvel = 15
        self.bulletdmglim = [20, 100]
        self.bulletdmgmultiplier = 0.1
        self.bulletcooldown = 15
        self.bulletcc = self.bulletcooldown
        self.ammo = 120
        self.ammotext = Text(100, 500, "Ammo: ", 30, (184,134,11), -1, self.ammo)
        self.bc = 1
        self.kk = 0
        self.hdl = 0

    def tire(self, cc, bullets):
        if not self.bulletcc >= self.bulletcooldown:
            self.bulletcc += 1
            return
        if self.ammo < 1:
            return
        self.bulletdmg = randint(self.bulletdmglim[0], self.bulletdmglim[1])     
        self.bulletdmg *= self.bulletdmgmultiplier
        self.bulletdmg = int(self.bulletdmg)
        self.bulletcc = 0
        self.milieu = (self.x, self.y)
        pygame.mixer.find_channel().play(pshot)#pygame.mixer.Sound.play(pshot)
        #calculs
        if (cc[0] - self.milieu[0]) == 0:
            if cc[1] > self.milieu[1]:
                bullets.append(Bullet((self.x), (self.y), [0, self.bulletvel], "player", self.bulletdmg, self.bc, self.bulletvel))
            else:
                bullets.append(Bullet((self.x), (self.y), [0, -self.bulletvel], "player", self.bulletdmg, self.bc, self.bulletvel))
            return
        angle = abs(atan((cc[1] - self.milieu[1]) / (cc[0] - self.milieu[0])))
        vels = [self.bulletvel * abs(cos(angle)), self.bulletvel * abs(sin(angle))]
        
        if cc[0] < self.milieu[0]:
            vels[0] = -abs(vels[0])
        else:
            vels[0] = abs(vels[0])
        if cc[1] < self.milieu[1]:
            vels[1] = -abs(vels[1])
        else:
            vels[1] = abs(vels[1])
        bullets.append(Bullet((self.x), (self.y), vels, "player", self.bulletdmg, self.bc, self.bulletvel))
        self.ammo -= 1
        self.ammotext.variable = self.ammo
    """   
    def distance(self, sh):
        return sqrt(((sh.x + sh.w//2) - (self.x + self.w//2)) ** 2 + ((sh.y + sh.h//2) - (self.y + self.h//2)) ** 2)
    
    def distance_of_2(self, fh, sh):
        return sqrt(((sh.x + sh.w//2) - (fh.x + fh.w//2)) ** 2 + ((sh.y + sh.h//2) - (fh.y + fh.h//2)) ** 2)
    """
    
    def draw(self, win, texts):
        if self.hp > self.maxhp:
            self.hdl += 1
        if self.hdl >= 60:
            self.hdl = 0
            self.hp -= 1
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(10, 10, 102, 37))
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(11, 11, 100, 35))
        if self.hp > 0: 
            pygame.draw.rect(win, (70, 255, 70), pygame.Rect(11, 11, self.hp, 35))
        if self.hp > self.maxhp:
            pygame.draw.rect(win, (105,105,105), pygame.Rect(11 + self.maxhp, 11, self.hp - self.maxhp, 35))#rgb(105,105,105), (64,224,208)
        self.ammotext.draw(win, texts)
        pygame.draw.circle(win, (60, 70, 170), (self.x, self.y), self.r)

class Enemy:
    def __init__(self, x, y, maxhp, bulletdmg, vel):
        #props(?)
        self.x = x
        self.y = y
        self.r = 1/3 * maxhp
        self.vel = vel
        self.maxhp = maxhp
        self.hp = self.maxhp
        self.mr, self.ml, self.mu, self.md = False, False, False, False
        self.milieu = (self.x, self.y)
        self.bulletvel = 10
        self.climit = 150
        self.counter = self.climit
        self.bulletdmg = bulletdmg
        #equation --> y = am + b
        #"hitboxes"
        #horizontal hitbox
        self.mh = 0.1 / self.r*2
        self.bh = self.y - self.x * self.mh
        #vertical hitbox
        #m = delta y / delta x
        self.mv = self.r*2 / 0.1
        self.bv = self.y - self.x * self.mv
        
    def distance(self, target):
        return sqrt((target.x - self.x)**2 + (target.y - self.y)**2)
    def tire(self, player, bullets, enemies):
        #equation --> y = am + b
        #"hitboxes"
        #horizontal hitbox
        self.bh = self.y - self.x * self.mh
        #vertical hitbox
        #m = delta y / delta x
        self.bv = self.y - self.x * self.mv



        if self.distance(player) > 164 + self.r:
            if player.x + self.r*2 < self.x or player.x - self.r*2 > self.x:
                if player.x + self.r*2 < self.x:
                    self.x -= self.vel
                else:
                    self.x += self.vel
            if player.y + self.r*2 < self.y or player.y - self.r*2 > self.y:
                if player.y + self.r*2 < self.y:
                    self.y -= self.vel
                else:
                    self.y += self.vel

        
        if self.counter >= self.climit:
            self.milieu = (self.x, self.y)
            cc = [player.x, player.y]
            #if player.md:
                #cc[0] +=
            eshot.set_volume(100/self.distance(player))
            pygame.mixer.find_channel().play(eshot)
            #calculs
            if (cc[0] - self.milieu[0]) == 0:
                if cc[1] > self.milieu[1]:
                    bullets.append(Bullet((self.x), (self.y), [0, self.bulletvel], "enemy", self.bulletdmg, 0, self.bulletvel))
                else:
                    bullets.append(Bullet((self.x), (self.y), [0, -self.bulletvel], "enemy", self.bulletdmg, 0, self.bulletvel))
                return
            angle = abs(atan((cc[1] - self.milieu[1]) / (cc[0] - self.milieu[0])))
            vels = [self.bulletvel * abs(cos(angle)), self.bulletvel * abs(sin(angle))]
            
            if cc[0] < self.milieu[0]:
                vels[0] = -abs(vels[0])
            else:
                vels[0] = abs(vels[0])
            if cc[1] < self.milieu[1]:
                vels[1] = -abs(vels[1])
            else:
                vels[1] = abs(vels[1])
            bullets.append(Bullet((self.x), (self.y), vels, "enemy", self.bulletdmg, 0, self.bulletvel))
            self.counter = 0
        else:
            self.counter += 1
    def draw(self, win):
        pygame.draw.circle(win, (232, 190, 172), (self.x, self.y), self.r)
        
    

class Wall:
    def __init__(self, x, y, w, h, colour):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.center = [self.x + self.w/2, self.y + self.h/2]
        self.colour = colour
        #equation --> y = am + b
        #"hitboxes"
        #the top horizontal line
        self.th = self.get_droite_equation((self.x, self.y), (self.x + self.w, self.y))
        #the bottom horizontal line
        self.bh = self.get_droite_equation((self.x, self.y + self.h), (self.x + self.w, self.y + self.h))
        #the western vertical line
        self.wv = self.get_droite_equation((self.x, self.y), (self.x, self.y + self.h))
        #the eastern vertical line
        self.ev = self.get_droite_equation((self.x + self.w, self.y), (self.x + self.w, self.y + self.h))

        self.droites = [self.th, self.bh, self.wv, self.ev]
        return

    def get_droite_equation(self, point1, point2):
        delta_y = point2[1] - point1[1]
        delta_x = point2[0] - point1[0]
        if delta_y == 0:
            delta_y = 0.1
        if delta_x == 0:
            delta_x = 0.1
        m = delta_y / delta_x
        b = point1[1] - point1[0] * m
        return [m, b, point1, point2]

    def update_b(self, point1, m):
        return point1[1] - point1[0] * m

    def update_bs(self):
        self.droites[0][1] = self.update_b((self.x, self.y), self.droites[0][0])
        self.droites[1][1] = self.update_b((self.x, self.y + self.h), self.droites[1][0])
        self.droites[2][1] = self.update_b((self.x, self.y), self.droites[2][0])
        self.droites[3][1] = self.update_b((self.x + self.w, self.y), self.droites[3][0])
        
    def detect_collision(self, player):
        if player.mr and player.x >= self.x - player.r - player.vel and player.x <= self.x:
            if player.y >= self.y - player.r and player.y <= self.y + self.h + player.r:
                player.mr = False
        if player.ml and player.x <= self.x + self.w + player.r + player.vel and player.x >= self.x + self.w:
            if player.y >= self.y - player.r and player.y <= self.y + self.h + player.r:
                player.ml = False
        if player.mu and player.y <= self.y + self.h + player.r + player.vel and player.y >= self.y + self.h:
            if player.x >= self.x - player.r and player.x <= self.x + self.w + player.r:
                player.mu = False
        if player.md and player.y >= self.y - player.r - player.vel and player.y <= self.y:
            if player.x >= self.x - player.r and player.x <= self.x + self.w + player.r:
                 player.md = False
        return

    def draw(self, win):
        self.center = [self.x + self.w/2, self.y + self.h/2]
        pygame.draw.rect(win, self.colour, pygame.Rect(self.x, self.y, self.w, self.h))


def enemy_wave_spawner(enemies, walls, enemy_counter, wave, enemy_randomizer_lims):
    enemy_counter += 1
    if enemy_counter == enemy_counter_limit or len(enemies) == 0:
        wave += 1
        for j in range(wave * 2):
            enemy_randomizer = [uniform(enemy_randomizer_lims[0], enemy_randomizer_lims[1]), int(uniform(enemy_randomizer_lims[2], enemy_randomizer_lims[3]))]
            enemy_spawn = choice(walls[4:])
            print("-----------------------------------")
            for brah in walls[4:]:
                print(brah.x, brah.y)
            enemies.append(Enemy(enemy_spawn.center[0], enemy_spawn.center[0], enemy_randomizer[0], enemy_randomizer[1], randint(1, 5)))
            for i in range(len(enemy_randomizer_lims)):
                if i == 0:
                    enemy_randomizer_lims[i] = enemy_randomizer_lims[i] * 0.5 + 10
                elif i == 1:
                    enemy_randomizer_lims[i] = enemy_randomizer_lims[i] * 0.5 + 50
                elif i == 2:
                    enemy_randomizer_lims[i] = enemy_randomizer_lims[i] * 0.5 + 2
                elif i == 3:
                    enemy_randomizer_lims[i] = enemy_randomizer_lims[i] * 0.5 + 15
            enemy_counter = 0

    return enemies, enemy_counter, wave, enemy_randomizer_lims




player = Human(300, 300)
humans = [player]
bullets = []
enemies = []#Enemy(10, 10, 100, -10000)]
texts = []



death_text =  Text(300, 200, f"GAME OVER! Killed {player.kk} enemies.", 30, (255, 0, 0), -1, "")

clock = pygame.time.Clock()
running = True
shooting = False
shooting_speed = 1
fps = 60
p_l, p_r, p_u, p_d = False, False, False, False
while running:
    clock.tick(fps)
    enemies, enemy_counter, wave, enemy_randomizer_lims = enemy_wave_spawner(enemies, walls, enemy_counter, wave, enemy_randomizer_lims)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
        if player.alive:
            if event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN:# and pygame.FINGERMOVE:#mouse_pos = pygame.mouse.get_pos()
                shooting = True
                player.bulletcc = player.bulletcooldown
            elif event.type == pygame.FINGERUP or event.type == pygame.MOUSEBUTTONUP:
                shooting = False
                player.cc = player.bulletcooldown
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p_l = True
                    player.ml = True
                if event.key == pygame.K_RIGHT:
                    p_r = True
                    player.mr = True
                if event.key == pygame.K_UP:
                    p_u = True
                    player.mu = True
                if event.key == pygame.K_DOWN:
                    p_d = True
                    player.md = True
                for wall in walls:
                    wall.detect_collision(player)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    p_l = False
                    player.ml = False
                if event.key == pygame.K_RIGHT:
                    p_r = False
                    player.mr = False
                if event.key == pygame.K_UP:
                    p_u = False
                    player.mu = False
                if event.key == pygame.K_DOWN:
                    p_d = False
                    player.md = False
        else:
            player.ml, player.md, player.mu, player.mr = False, False, False, False
            shooting = False

    if True in [player.md, player.mu, player.mr, player.ml]:
        if player.ml:
            for liste in [bullets, enemies, texts, bonuses, walls]:
                for element in liste:
                    element.x += player.vel
        if player.mr:
            for liste in [bullets, enemies, texts, bonuses, walls]:
                for element in liste:
                    element.x -= player.vel
        if player.mu:
            for liste in [bullets, enemies, texts, bonuses, walls]:
                for element in liste:
                    element.y += player.vel
        if player.md:
            for liste in [bullets, enemies, texts, bonuses, walls]:
                for element in liste:
                    element.y -= player.vel

    if shooting:
        mouse_pos = pygame.mouse.get_pos()
        player.tire(mouse_pos, bullets)
        
    if player.alive:
        if p_l:
            player.ml = True
        if p_r:
            player.mr = True
        if p_d:
            player.md = True
        if p_u:
            player.mu = True
    else:
        player.ml = False
        player.mr = False
        player.md = False
        player.mu = False
    for wall in walls:
        wall.detect_collision(player)
        
    if not running:
        break
    win.fill((30, 30, 30))#(160, 70, 70))
    
    
    for enemy in enemies:
        enemy.draw(win)
        enemy.tire(player, bullets, enemies)
    #for bonus in bonuses:
        #bonus.draw(win, player, bonuses, texts)
    for wall in walls:
        wall.update_bs()
        wall.draw(win)
    for human in humans:
        human.draw(win, texts)
    for bullet in bullets:
        bullet.toucher(enemies, player, bullets, texts, bonuses, walls)
        bullet.avancer()
        bullet.draw(win)
    for text in texts:
        text.draw(win, texts)
    if not player.alive:
        death_text.draw(win, texts)

    pygame.display.flip()










