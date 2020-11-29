import pygame
import random
import sys
pygame.init()

Width = 800
Height = 600

Red = (255,0,0)
Blue = (0,0,255)
s_color = (255,85,0)
Background_Color = (11,235,205)

player_size = 50
player_pos = [Width/2, Height -1.5*player_size]

enemy_size = 50
enemy_pos = [random.randint(0,Width-player_size), 0]
enemy_list = [enemy_pos]

screen = pygame.display.set_mode((Width, Height))

game_over = False

clock = pygame.time.Clock() 
speed = 10

myFont = pygame.font.SysFont("monospace", 35)

score = 0

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay< 0.15 :
        x_p = random.randint(0, Width-enemy_size)
        y_p = 0
        enemy_list.append([x_p, y_p])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
         pygame.draw.rect(screen, Blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_position(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < Height:
            enemy_pos[1] += speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (p_x <= e_x and e_x < (p_x+player_size)) or (e_x <= p_x and p_x < (e_x + enemy_size) ):
        if (e_y >= p_y and e_y < (p_y+player_size) ) or ( e_y<= p_y and p_y < (e_y + enemy_size) ):
            return True
    return False

def set_level(score,speed):
    if score < 10:
        speed = 5
    elif score < 20:
        speed = 8
    elif score < 40:
        speed = 13;
    elif score <= 60:
        speed = 20
    else :
        speed = 27
    # speed = score/5 +1
    return speed

while not game_over:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_pos[0]-= player_size
                   
                elif event.key == pygame.K_RIGHT:
                    player_pos[0]+= player_size
                
    screen.fill(Background_Color)

    # updating position of single enemy
    # if enemy_pos[1] >= 0 and enemy_pos[1] < Height:
    #     enemy_pos[1] += speed
    # else:
    #     enemy_pos[0] = random.randint(0, Width-enemy_size)
    #     enemy_pos[1] = 0

    
    drop_enemies(enemy_list)
    score = update_enemy_position(enemy_list, score)

    speed = set_level(score, speed)

    text = "Score: " + str(score)
    label = myFont.render(text, 1, s_color )
    screen.blit(label, (Width-200, Height-40))

    if collision_check(enemy_list, player_pos) :
        game_over = True
        print('Final Score:',score)
        break

    draw_enemies(enemy_list)
    pygame.draw.rect(screen, Red, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()

