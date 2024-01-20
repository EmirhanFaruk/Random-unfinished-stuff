
# Modification date: Thu May 26 15:02:32 2022

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




ww = 600
wh = 600
win = pygame.display.set_mode((ww, wh))
pygame.init()

eshot = pygame.mixer.Sound("eshot.wav")
pshot = pygame.mixer.Sound("pshot.wav")
pygame.mixer.set_num_channels(10000)


class Blood:
    def __init__(self, x, y, r, colour, duration):
        self.x, self.y, self.r, self.colour, self.duration = x, y, r, colour, duration

    def draw(self, win, bloods):
        if self.duration == 0:
            bloods.remove(self)
            return
        self.duration -= 1
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.r)
        

class Text:
    def __init__(self, x, y, text, size, colour, duration, variable, speed = 0):
        self.x, self.y, self.size, self.colour, self.duration, self.speed = x, y, size, colour, duration, speed
        self.text = text
        self.variable = variable
        self.font = pygame.font.SysFont('Comic Sans MS', self.size)
        self.text_surface = self.font.render(self.text, False, self.colour)
        self.text_width = self.text_surface.get_width()

    def draw(self, win, texts):
        if self.duration == 0:
            texts.remove(self)
        if self.duration != -1:
            self.duration -= 1
        self.text_surface = self.font.render(self.text + str(self.variable), False, self.colour)
        self.text_width = self.text_surface.get_width()
        win.blit(self.text_surface, (self.x - self.text_width/2, self.y))
        self.y -= self.speed
        return

"""
class Bonus:
    def __init__(self, x, y, the_bonus):
        self.x, self.y, self.the_bonus = x, y, the_bonus
        self.r = 8
        self.duration = 300
        if self.the_bonus == "+health":
            self.colour = (50, 255, 50)
        elif self.the_bonus == "+1 bullet":
            self.colour = (200, 200, 50)
        elif self.the_bonus == "+speed":
            self.colour = (64,224,208)
        elif self.the_bonus == "+shooting speed":
            self.colour = (150, 150, 0) 
        
    def distance(self, target):
        return sqrt((target.x - self.x)**2 + (target.y - self.y)**2)
    def draw(self, win, player, bonuses, texts):
        self.duration -= 1
        if self.duration <= 0:
            bonuses.remove(self)
            return
        if self.distance(player) < self.r + player.r:
            if self.the_bonus == "+health":
                player.hp += 25
            elif self.the_bonus == "+1 bullet":
                player.bc += 1
                if player.bc > 10:
                    player.bc = 10
            elif self.the_bonus == "+speed":
                player.vel += 0.2
                if player.vel > 8:
                    player.vel = 8
            elif self.the_bonus == "+shooting speed":
                player.bulletcooldown -= 1
                if player.bulletcooldown < 1:
                    player.bulletcooldown = 1
            texts.append(Text(self.x - self.r, self.y, self.the_bonus, 20, self.colour, 50, 0.4))
            bonuses.remove(self)
            return
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.r)
"""
            
    

class Bullet:
    def __init__(self, x, y, vels, source, damage, count, bulletvel):
        self.x, self.y, self.vels = x, y, vels
        self.r = 2
        self.source = source
        self.damage = damage
        self.counting = 0
        self.limit = 300
        self.number = count
        self.bulletvel = bulletvel
        #equation --> y = am + b
        the = False
        if self.vels[0] == 0:
            self.vels[0] = 0.1
            the = True
        self.m = self.vels[1]/self.vels[0]
        if the:
            self.vels[0] = 0
        self.b = self.y - self.x * self.m 

    def distance(self, target):
        return sqrt((target.x - self.x)**2 + (target.y - self.y)**2)
    def distancexy(self, x, y):
        return sqrt((x - self.x)**2 + (y - self.y)**2)
    def old_distance(self, target):
        return sqrt((target.x - (self.x - self.vels[0]))**2 + (target.y - (self.y - self.vels[1]))**2)

    def detect_intersection_round(self, target, tx, ty, tr, tm, tb, cases):
        if self.distance(target) < sqrt(self.vels[0]**2 + self.vels[1]**2) and not any(cases):
            if tm != self.m and not any(cases):
                point_dintersection_x = (tb - self.b) / (self.m - tm)
                point_dintersection_y = point_dintersection_x * tm + tb
                if sqrt((point_dintersection_x - tx)**2 + (point_dintersection_y - ty)**2) < tr:
                    if (self.vels[0] >= 0 and self.x <= point_dintersection_x) or (self.vels[0] <= 0 and self.x >= point_dintersection_x):#checking x vels etc to prevent "backshooting"
                        if (self.vels[1] >= 0 and self.y <= point_dintersection_y) or (self.vels[1] <= 0 and self.y >= point_dintersection_y):#checking y vels etc to prevent "backshooting"
                            cases.append(True)
                            return cases, (point_dintersection_x, point_dintersection_y), self.distancexy(point_dintersection_x, point_dintersection_y)
        return cases, (-100, -100), 99999
    def detect_intersection_rectangle(self, target, cases):
        for droite in target.droites:
            if droite[0] != self.m and not any(cases):
                point_dintersection_x = (droite[1] - self.b) / (self.m - droite[0])
                point_dintersection_y = point_dintersection_x * droite[0] + droite[1]
                if ((point_dintersection_x >= droite[3][0] or point_dintersection_x <= droite[2][0]) or (point_dintersection_x <= droite[3][0] or point_dintersection_x >= droite[2][0])):
                    if ((point_dintersection_y >= droite[3][1] or point_dintersection_y <= droite[2][1]) or (point_dintersection_y <= droite[3][1] or point_dintersection_y >= droite[2][1])):
                        if point_dintersection_x >= target.x - 1 and point_dintersection_x <= target.x + target.w + 1 and point_dintersection_y >= target.y - 1 and point_dintersection_y <= target.y + target.h + 1:
                            if self.distancexy(point_dintersection_x, point_dintersection_y) < self.bulletvel:
                                if (self.vels[0] >= 0 and self.x <= point_dintersection_x) or (self.vels[0] <= 0 and self.x >= point_dintersection_x):#checking x vels etc to prevent "backshooting"
                                    if (self.vels[1] >= 0 and self.y <= point_dintersection_y) or (self.vels[1] <= 0 and self.y >= point_dintersection_y):#checking y vels etc to prevent "backshooting"
                                        cases.append(True)
                                        return cases, (point_dintersection_x, point_dintersection_y), self.distancexy(point_dintersection_x, point_dintersection_y)
        return cases, (-100, -100), 99999
    def toucher(self, enemies, player, bullets, texts, bonuses, walls):
        #equation --> y = am + b
        the = False
        if self.vels[0] == 0:
            self.vels[0] = 0.000001
            the = True
        self.m = self.vels[1]/self.vels[0]
        if the:
            self.vels[0] = 0
        self.b = self.y - self.x * self.m
        
        self.counting += 1
        if self.limit < self.counting:
            bullets.remove(self)
            return
        wall_i_list = []
        wall_pd_list = []
        wall_cases = []
        for wall in walls:
            wall_cases, new_pd, new_i = self.detect_intersection_rectangle(wall, wall_cases)
            wall_i_list.append(new_i)
            wall_pd_list.append(new_pd)
        wall_min_i = min(wall_i_list) 
        wall_min_pd = wall_pd_list[wall_i_list.index(wall_min_i)]
        if self.source == "player":
            for enemy in enemies:
                cases = [self.distance(enemy) < self.r + enemy.r, self.old_distance(enemy) < self.r + enemy.r]
                cases, pd1, i1 = self.detect_intersection_round(enemy, enemy.x, enemy.y, enemy.r, enemy.mh, enemy.bh, cases)
                cases, pd2, i2 = self.detect_intersection_round(enemy, enemy.x, enemy.y, enemy.r, enemy.mv, enemy.bv, cases)
                if i1 < i2:
                    le_i = i1
                    le_pd = pd1
                else:
                    le_i = i2
                    le_pd = pd2
                
                
                if any(cases):
                    if wall_min_i < le_i:
                        pygame.draw.circle(win, (255, 255, 0), wall_min_pd, self.r)
                        bullets.remove(self)
                        return
                    
                    while self.number > 0 and enemy.hp > 0:
                        self.number -= 1
                        enemy.hp -= self.damage
                        pygame.draw.circle(win, (255, 0, 0), le_pd, enemy.r//3)
                        if enemy.hp <= 0:
                            texts.append(Text(randint(int(enemy.x - enemy.r * 2), int(enemy.x + enemy.r * 2)), randint(int(enemy.y - enemy.r * 2), int(enemy.y + enemy.r * 2)), "-" + str(self.damage), 10, (255, 50, 50), 30, "", 0.3))
                            break
                        else:
                            texts.append(Text(randint(int(enemy.x - enemy.r * 2), int(enemy.x + enemy.r * 2)), randint(int(enemy.y - enemy.r * 2), int(enemy.y + enemy.r * 2)), "-" + str(self.damage), 10, (255, 100, 100), 30, "", 0.3))
                    if enemy.hp <= 0:
                        player.ammo += 5
                        if player.ammo > 120:
                            player.ammo = 120
                        pygame.draw.circle(win, (255, 0, 0), le_pd, enemy.r//3)#make blood drop
                        enemies.remove(enemy)
                        player.hp += 1
                        player.kk += 1
                        print(f"\n--------------------------\nKilled {player.kk} enemies\n-Health = {player.hp}\n-Bullet count = {player.bc}\n-Speed = {player.vel}\n-Shooting speed = 1 bullet per {player.bulletcooldown} frame(s)\nBullet velocity = {player.bulletvel}\nBullet damage multiplier = {player.bulletdmgmultiplier}\nAmmo = {player.ammo}")
                        chosen = False
                        if True:#randint(1, 5) == 2:
                            while not chosen:
                                dab = choice(["+health", "+1 extra bullet", "+speed", "+shooting speed", "+bullet velocity", "+damage multiplier", "+30 ammo"])
                                colour = (50, 255, 50)
                                if dab == "+health":
                                    player.hp += 25
                                    chosen = True
                                elif dab == "+1 extra bullet":
                                    player.bc += 1
                                    if player.bc > 4:
                                        player.bc = 4
                                    else:
                                        chosen = True
                                elif dab == "+speed":
                                    player.vel += 0.2
                                    if player.vel > 8:
                                        player.vel = 8
                                    else:
                                        chosen = True
                                elif dab == "+shooting speed":
                                    if player.bulletcooldown > 5:
                                        player.bulletcooldown -= 1
                                        chosen = True
                                elif dab == "+bullet velocity":
                                    if player.bulletvel < 300:
                                        player.bulletvel += 2
                                        chosen = True
                                elif dab == "+damage multiplier":
                                    if player.bulletdmgmultiplier < 10:
                                        player.bulletdmgmultiplier += 0.05
                                        chosen = True
                                elif dab == "+30 ammo":
                                    player.ammo += 30
                                    if player.ammo > 120:
                                        player.ammo = 120
                                    else:
                                        chosen = True
                                    player.ammotext.variable = player.ammo
                            texts.append(Text(player.x - player.r, player.y, dab, 20, colour, 50, "", 0.4))
                    if self.number < 1:
                        bullets.remove(self)
                    return
            if any(wall_cases):
                pygame.draw.circle(win, (255, 255, 0), wall_min_pd, self.r)
                bullets.remove(self)
                return
        else:
            if self.distance(player) < self.r + player.r:
                player.hp -= self.damage
                if player.hp <= 0:
                    player.hp = 0
                    player.alive = False
                    
                else:
                    texts.append(Text(randint(player.x - player.r * 2, player.x + player.r * 2), randint(player.y - player.r * 2, player.y + player.r * 2), "-" + str(self.damage), 10, (255, 100, 100), 30, "", 0.3))
                bullets.remove(self)
                return
            if any(wall_cases):
                pygame.draw.circle(win, (255, 255, 0), wall_min_pd, self.r)
                bullets.remove(self)
                return
    def avancer(self):
        self.x += self.vels[0]
        self.y += self.vels[1]

    def draw(self, win):
        coef = uniform(0.7, 4)
        pygame.draw.line(win, (255,255,0), (self.x, self.y), (self.x - self.vels[0]/coef, self.y - self.vels[1]/coef))#old colour: (160, 70, 70)




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
bonuses = []
walls = []

walls.append(Wall(player.x - 1000, player.y - 1000, 2000, 300, (0, 0, 0)))#top wall
walls.append(Wall(player.x - 1000, player.y - 1000, 300, 2000, (0, 0, 0)))#west wall
walls.append(Wall(player.x + 1000, player.y - 1000, 300, 2000, (0, 0, 0)))#east wall
walls.append(Wall(player.x - 1000, player.y + 1000, 2000, 300, (0, 0, 0)))#bottom wall
walls.append(Wall(player.x - 700, player.y - 700, 300, 300, (100, 100, 100)))#Enemy spawn
walls.append(Wall(player.x + 700, player.y - 700, 300, 300, (100, 100, 100)))#Enemy spawn
walls.append(Wall(player.x - 700, player.y + 700, 300, 300, (100, 100, 100)))#Enemy spawn
walls.append(Wall(player.x + 700, player.y + 700, 300, 300, (100, 100, 100)))#Enemy spawn



death_text =  Text(300, 200, f"GAME OVER! Killed {player.kk} enemies.", 30, (255, 0, 0), -1, "")

clock = pygame.time.Clock()
running = True
#ayeee = 0
#compteur = 0
enemy_counter = 0
enemy_counter_limit = 600
enemy_randomizer_lims = [30, 50, 1, 10]
wave = 0
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










