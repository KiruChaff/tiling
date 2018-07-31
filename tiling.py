import random, sys
n=11
iter=chr(65)
missing_spot=[]
def createGrid(n):
    grid=[]
    for i in range(2**n):
        grid.append([])
        for j in range(2**n):
            grid[i].append(None)
    rand_y=random.randrange(2**n);rand_x=random.randrange(2**n)
    grid[rand_y][rand_x]=" "
    # grid[1][2]=" "
    return grid
grid=createGrid(n)
def fill(s_y=0, v_y=len(grid)-1, s_x=0, v_x=len(grid)-1, n=len(grid)-1):
    global iter
    if n==0:
        return
    missing_spot=find_missing_spot(s_y, v_y, s_x, v_x)
    fill_center(s_y, v_y, s_x, v_x, missing_spot)
    if ord(iter)>=90:
        iter=chr(65)
    else: iter=chr(ord(iter)+1)
    fill(s_y, ((v_y-s_y)//2)+s_y, s_x, ((v_x-s_x)//2)+s_x, n//2)
    fill(s_y, ((v_y-s_y)//2)+s_y, (((v_x-s_x)//2)+s_x)+1, v_x, n//2)
    fill((((v_y-s_y)//2)+s_y)+1, v_y, s_x, ((v_x-s_x)//2)+s_x, n//2)
    fill((((v_y-s_y)//2)+s_y)+1, v_y, (((v_x-s_x)//2)+s_x)+1, v_x, n//2)
    return
def find_missing_spot(s_y, v_y, s_x, v_x):
    x=0
    y=0
    for i in range(s_y, v_y+1):
        for j in range(s_x, v_x+1):
            if grid[i][j]!=None:
                if i>(((v_y-s_y)//2)+s_y):# XXX:
                    y+=1
                if j>(((v_x-s_x)//2)+s_x):# XXX:
                    x+=1
                return [x, y]
def fill_center(s_y, v_y, s_x, v_x, spot):
    x=(s_x//2)+(v_x//2);y=(s_y//2)+(v_y//2);
    square_x=0;square_y=0;
    for i in range(4):
        if spot!=[square_x,square_y]:
            grid[y][x]=iter
        if square_x<1:
            square_x+=1
            x+=1
        else:
            square_y+=1
            square_x-=1
            y+=1
            x-=1
    return
def display_grid(grid):
    for i in range(len(grid)):
        result=""
        for j in range(len(grid)):
            if grid[i][j]!=None:
                result+=str(grid[i][j])+" "
        import time;time.sleep(.05)
        print(result)
fill()
display_grid(grid)
