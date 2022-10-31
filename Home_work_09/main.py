import pygame
import random

pygame.init()

def draw_grit(scr):
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 3)

def draw_xo(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == "0":
                pygame.draw.circle(scr, (255, 96, 208), (j * 100 + 50, i * 100 + 50), 45)
            elif items [i][j] == "x":
                pygame.draw.line(scr, (96, 255, 128), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95),3)
                pygame.draw.line(scr, (96, 255, 128), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95),3)  

def get_win_check(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True                
    for i in range(3):
        if fd[0][i]  == fd[1][i] == fd[2][i] == symbol:
            flag_win = True
    if fd[0][0]  == fd[1][1] == fd[2][2] == symbol:
        flag_win = True    
    if fd[0][2]  == fd[1][1] == fd[2][0] == symbol:
        flag_win = True  
    return flag_win          

screen_size = (300, 300) 

window = pygame.display.set_mode(screen_size) 
screen = pygame.Surface(screen_size)

pygame.display.set_caption("Крестики-нолики") 
screen.fill((255, 255, 255))

field = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
mainloop = True
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == "":    
                field[pos[1] // 100][pos[0] // 100] = "x"
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "0"  

            player_win = get_win_check(field, "x")
            comp_win = get_win_check(field, "0")
            
            if player_win or comp_win:
                if player_win:
                    pygame.display.set_caption("Вы выиграли!!!!!!")
                else:
                    pygame.display.set_caption("Искусственный интеллект сделал тебя! Иди тренеруйся")
            elif field[0].count("x") + field[0].count("0") + field[1].count("x") + \
                    field[1].count("0") + field[2].count("x") + field[2].count("0") == 8:
                pygame.display.set_caption("Ничья")    


    draw_xo(screen, field)
    draw_grit(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()                 