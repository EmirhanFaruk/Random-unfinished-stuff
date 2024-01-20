import pygame
import random
import os

h = 720
w = 1000
"""
w, h = pygame.display.get_surface().get_size()
w = w // 2
h = h // 2
"""
#pygame.display.set_mode((0,0),pygame.FULLSCREEN)
win = pygame.display.set_mode((w,h))
pygame.init()

#icon and title
pygame.display.set_caption("Zıpzıp")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

def main():
    # Font
    font = pygame.font.Font("freesansbold.ttf", 20)


    def show_score(x, y, score):
        score = font.render("Score: " + str(score), True, (50, 100, 250))
        win.blit(score, (x, y))


    # Game Over text
    over_font = pygame.font.Font("freesansbold.ttf", 64)


    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (200, 0, 0))
        win.blit(over_text, (w//3-50, h//5))

    def start_button():
        start_text = over_font.render("START", True, (50, 50, 255))
        win.blit(start_text, (w//3+60, h//4*3+40))

    def high_score_text():
        start_text = over_font.render("  High Score: " + str(high_score), True, (100, 100, 255))
        win.blit(start_text, (w//4, h//3))
    
    def retry_button():
        start_text = over_font.render("RETRY", True, (50, 50, 255))
        win.blit(start_text, (w//3+60, h//4*3+40))

    def de_tree_things(enemy, i = 0):
        da_tree_body_x = random.randint(enemy.x - 500, enemy.x - 200)
        da_tree_body_y = random.randint(550, 600)
        da_tree_body_w = random.randint(25, 75)
        da_tree_body_h = 700 - da_tree_body_y
        da_tree_leaves_x = da_tree_body_x - random.randint(50, 150)
        da_tree_leaves_y = da_tree_body_y - random.randint(10, 40)
        da_tree_leaves_w = da_tree_body_w + (2 * da_tree_body_x - da_tree_leaves_x)
        da_tree_leaves_h = da_tree_leaves_y + random.randint(da_tree_body_h // 5, da_tree_body_h // 4)
        da_tree_body_colour = ((139-(i * 2), 69-(i * 2), 19-(i * 2)))
        da_tree_leaves_colour = (86-(i * 2), 224-(i * 2), 0)
        return [da_tree_body_x, da_tree_body_y, da_tree_body_w, da_tree_body_h, da_tree_leaves_x, da_tree_leaves_y, da_tree_leaves_w, da_tree_leaves_h, da_tree_body_colour, da_tree_leaves_colour]

    class Rectangle:
        def __init__(self, x, y, w, h, colour, speed = random.randint(3, 7)):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.colour = colour
            self.r = int(colour[0])
            self.g = int(colour[1])
            self.b = int(colour[2])
            self.speed = speed
            self.isJumping = False
            self.going = "up"
            self.alive = True
            #self.JumpingN = 1
        def move(self, speed, direction):
            if direction == "left":
                self.x -= speed
        def jump(self, jheight):
            if self.isJumping:
                if self.going == "up":
                    if self.y >= 700 - self.h - jheight:
                        self.y -= 5
                    else:
                        self.going = "down"
                else:
                    if self.y > 700 - self.h:
                        self.isJumping = False
                        self.going = "up"
                    else:
                        self.y += 4
        def collision(self, other):
            if (self.w + self.x > other.x) and (self.y + self.h > other.y) and (self.x < other.x):
                return False
            else:
                return True
        def prs(self):
            #pygame.draw.rect(win, (rgb_value_list[0], rgb_value_list[1], rgb_value_list[2]), (x1, y1, x2, y2))
            pygame.draw.rect(win, (self.r, self.g, self.b), (self.x, self.y, self.w, self.h))
	



    player = Rectangle(100, 600, 50, 100, (0, 200, 0))
    enemy = Rectangle(1200, 650, 25, 50, (200, 0, 0))
    new_speed = 3

    ground = Rectangle(0, 700, 2000, 1000, (40, 170, 70))
    clouds = []
    for i in range(4):
        clouds.append(Rectangle(random.randint(1500, 2000), random.randint(0, 300), random.randint(200, 400), random.randint(100, 200), (235+i*5, 235+i*5, 255)))

    button = Rectangle(w//3, h//4*3, w//3, h//5, (200, 220, 120))

    
    tree = []
    for i in range(1):
        tree_prop = de_tree_things(enemy, i)
        tree.append(Rectangle(tree_prop[4], tree_prop[5], tree_prop[6], tree_prop[7], tree_prop[9], enemy.speed))
        tree.append(Rectangle(tree_prop[0], tree_prop[1], tree_prop[2], tree_prop[3], tree_prop[8], enemy.speed))
        
    







    clock = pygame.time.Clock()



    running = True
    playing = False
    entered_point = False
    score = 0
    logged = False
    high_score = 0
    fs = 4
    ls = 7
    enemy_down = False
    for i in range(len(clouds)):
        clouds[i].x = -500
    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN and playing:
                if not player.isJumping:
                    player.isJumping = True
            if event.type == pygame.MOUSEBUTTONDOWN and not playing:
                pos = pygame.mouse.get_pos()
                #print(pos)
                if pos[0] > w//3 and pos[0] < w//3 * 2 and pos[1] > h//4*3 and pos[1] < (h//4*3) + h//5:
                    playing = True
            if event.type == pygame.FINGERDOWN and not playing:
                pos = (event.x * w, event.y * h)
                #print(pos)
                if pos[0] > w//3 and pos[0] < w//3 * 2 and pos[1] > h//4*3 and pos[1] < (h//4*3) + h//5:
                    playing = True
            if event.type == pygame.MOUSEBUTTONDOWN and not(player.alive):
                pos = pygame.mouse.get_pos()
                #print(pos)
                if pos[0] > w//3 and pos[0] < w//3 * 2 and pos[1] > h//4*3 and pos[1] < (h//4*3) + h//5:
                    return True
            if event.type == pygame.FINGERUP and not(player.alive):
                pos = (event.x * w, event.y * h)
                #print(pos)
                if pos[0] > w//3 and pos[0] < w//3 * 2 and pos[1] > h//4*3 and pos[1] < (h//4*3) + h//5:
                    return True
    
        if playing:
            player.alive = player.collision(enemy)

            if player.alive:
                player.jump(100)
                if enemy.x + enemy.w > 0:
                    enemy.move(new_speed, "left")
                else:
                    enemy_down = True
                    new_speed = random.randint(fs, ls)
                    fs += 1
                    ls += 1
                    enemy.x = random.randint(1000, 1500)
                    entered_point = False
                if enemy.x < player.x and not entered_point:
                    score += 1
                    entered_point = True
            else:
                if not logged:
                    file = open("scores.txt", "a")
                    file.write(str(score) + "\n")
                    file.close()
                    with open("scores.txt") as f:
                        lines = f.readlines()
                        f.close()
                    for i in range(len(lines)):
                        lines[i] = lines[i].strip("\n")
                        lines[i] = int(lines[i])
                    lines.sort()
                    high_score = lines[-1]
                    os.remove("scores.txt")
                    file = open("scores.txt", "w")
                    file.write(str(high_score) + "\n")
                    file.close()
                    logged = True
                
                

            
            for i in range(len(clouds)):
                if clouds[i].x > - clouds[i].w :
                    clouds[i].move(clouds[i].speed, "left")
                else:
                    clouds[i].speed = random.randint(2, 7)
                    clouds[i].x = random.randint(1500, 2000)
                    clouds[i].y = random.randint(0, 300)

            for i in range(len(tree)):
                if enemy_down:
                    tree_prop = de_tree_things(enemy, i)
                    tree[i] = Rectangle(tree_prop[4], tree_prop[5], tree_prop[6], tree_prop[7], tree_prop[9], enemy.speed)
                    tree[i] = Rectangle(tree_prop[0], tree_prop[1], tree_prop[2], tree_prop[3], tree_prop[8], enemy.speed)
                    enemy_down = False
                else:
                    for i in range(2):
                        tree[i].move(new_speed, "left")



            win.fill((0, 200, 255))
            for i in range(-1, 1):
                tree[i].prs()
            player.prs()
            enemy.prs()
            ground.prs()
            for i in range(len(clouds)):
                clouds[i].prs()
            show_score(10, 10, score)
            if not player.alive:
                game_over_text()
                high_score_text()
                button.prs()
                retry_button()
            pygame.display.flip()



        else:
            for i in range(len(clouds)):
                if clouds[i].x > - clouds[i].w :
                    clouds[i].move(clouds[i].speed, "left")
                else:
                    clouds[i].speed = random.randint(2, 7)
                    clouds[i].x = random.randint(1000, 2000)
                    clouds[i].y = random.randint(0, 300)

            win.fill((0, 200, 255))
            ground.prs()
            for i in range(len(clouds)):
                clouds[i].prs()
            button.prs()
            start_button()
            pygame.display.flip()

playing_da_game = True
while playing_da_game:
    playing_da_game = main()