# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 0]  # cost has 3 values, corresponding to making
cost1 =1

# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]

    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    # v2d = [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    print 'Generate heuristic policy ========'
    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                print '.'
                # vMin = 999
                # aMin = -1
                for f in range(len(forward)):
                    if goal[0] == x and goal[1] == y:
                        if value[f][x][y] > 0:
                            value[f][x][y] = 0
                            policy2D[x][y]='*'
                            change = True

                    elif grid[x][y] == 0:

                        for a in range(len(action)):
                            ## big meat changes here
                            # how's action impact coordinate and value map?
                            f2 = f+action[a]
                            x2 = x + forward[f2%4][0]
                            y2 = y + forward[f2%4][1]

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[f2%4][x2][y2] + cost[a]

                                if v2 < value[f][x][y]:
                                    change = True

                                    print 'x:y:f ',x,':',y,':',f,' ',action_name[a]
                                    # for i in policy:
                                    #     print i
                                    value[f][x][y] = v2
                                    print 'current:', forward_name[f]
                                    for i in value[f]:
                                        print i
                                    print 'next:', forward_name[f2%4]
                                    for i in value[f2%4]:
                                        print i


    for i in grid:
        print i

    print 'value map.'
    for i in range(len(value)):
        print forward_name[i]
        for j in value[i]:
            print j
    print
    print 'Running policy ============================================='
    print

    x=init[0]
    y=init[1]
    f=init[2]
    # count=0
    while x<>goal[0] or y<> goal[1]:
        # count+=1
        vmin=999
        amin=-1
        for i in range(len(action)):
            f2=f+action[i]
            x2 = x+forward[f2%4][0]
            y2 = y+forward[f2%4][1]

            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                if vmin>value[f2][x2][y2]+cost[i]:
                    vmin=value[f2][x2][y2]+cost[i]
                    amin=i

        policy2D[x][y]=action_name[amin]
        f = f + action[amin]
        x = x + forward[f % 4][0]
        y = y + forward[f % 4][1]

        print 'direction: xy directionValueMap action:',x,y,forward_name[f],action_name[amin]

    print 'policy:'
    for i in policy2D:
        print i

    return policy2D

optimum_policy2D(grid, init, goal, cost)