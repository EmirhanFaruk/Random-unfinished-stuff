
# Modification date: Tue Dec 20 22:35:20 2022

# Production date: Sun Sep  3 15:44:14 2023

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
                        
                    if self.number < 1:
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
				
    def avancer(self):
        self.x += self.vels[0]
        self.y += self.vels[1]

    def draw(self, win):
        coef = uniform(0.7, 4)
        pygame.draw.line(win, (255,255,0), (self.x, self.y), (self.x - self.vels[0]/coef, self.y - self.vels[1]/coef))#old colour: (160, 70, 70)
