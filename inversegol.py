import pygame
import random


CELL_COLOR = (132, 177, 219)
BLACK = (0,0,0)
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Conways Game of Life')
screen.fill(BLACK)
GENERATION = 0

num = size[0]//25 #for 28x28 pixel cells
#Rectangle Objects
rects = [list([pygame.Rect(x,y,25,25) for y in range(0,700,25)]) for x in range(0,700,25)]
#Map of which cells are alive and which are dead
state_map = [list([0 for r in range(len(rects))]) for c in range(len(rects[0]))] 

#Get starting points from the text file
start_pos = []
with open('startingpoints.txt','r',encoding = 'utf-8') as f:
    for line in f:
        file_line = line.split(',')
        points = (file_line[0],file_line[1])
        start_pos.append(points)

for (r,c) in start_pos:
    state_map[int(r)][int(c)] = 1
#Main loop
done = False
while not done:
    pygame.time.wait(1000)
    screen.fill(BLACK)
    print(GENERATION)
    GENERATION += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for i in range(len(state_map)):
        for j in range(len(state_map[0])):
            if state_map[i][j] == 0:
                pygame.draw.rect(screen, CELL_COLOR,rects[i][j])
            else:
                pygame.draw.rect(screen, CELL_COLOR,rects[i][j],2)
    changes = {}
    #Get neighboring cell states and find number of neighbors
    for r in range(len(state_map)):
        for c in range(len(state_map)):
            num_neighbors = 0
            r_shift = [-1,1,0]
            c_shift = [-1,1,0]
            if r%27==0:
                if r/27 == 0:
                    r_shift[0] = 27
                elif r/27 == 1:
                    r_shift[1] = -27
            if c%27==0:
                if c/27==0:
                    c_shift[0] = 27
                elif c/27 == 1:
                    c_shift[1] = -27

            for i in r_shift:
                for j in c_shift:
                    if (i,j) == (0,0):
                        pass
                    else:
                        num_neighbors += state_map[r+i][c+j]
        #Check rules    
            if state_map[r][c] == 0:
                if num_neighbors < 2 or  num_neighbors > 3: 
                    changes[(r,c)]= 1
            elif state_map[r][c] == 1:
                if num_neighbors == 3:
                    changes[(r,c)]= 0
    #Swap in new states
    for c in changes:
        r,c = c[0],c[1]
        state_map[r][c] = changes[(r,c)]


    pygame.display.flip()


