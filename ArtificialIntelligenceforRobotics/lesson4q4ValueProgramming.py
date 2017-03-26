# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    value[goal[0]][goal[1]]=0
    steps = []
    steps.append(goal)

    loop =0
    while(len(steps)>0 and loop < 100):
        loop+=1
        start = steps.pop()
        # print 'start:',start
        for i in range(len(delta)):
            x = start[0]+delta[i][0]
            y = start[1]+delta[i][1]
            if(x>=0 and x<len(grid) and y>=0 and y<len(grid[0])):
                if(grid[x][y]<>1 and value[x][y]>value[start[0]][start[1]]+cost):
                    value[x][y]=value[start[0]][start[1]]+cost
                    action[x][y]=i
                    # print 'next: ', [x, y],' v:', value[x][y]
                    steps.append([x,y])


    return value

vs = compute_value(grid, goal, cost)
for i in vs:
    print i