# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
# grid=[[0,1],
#       [0,0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    # print 'grid: ',valueOf(grid, init)
    nodes = []
    init.append(0)
    nodes.append(init)

    i=0

    while(len(nodes)>i):
        node = nodes[i]
        i += 1
        print 'checking node, ',node
        delta_len = len(delta)
        for j in range(delta_len):
            newNode=move(node, cost, delta[j])
            if(isGoal(goal, newNode)):
                # print newNode
                return newNode

            if(isNavigable(grid, nodes, newNode)):
                print 'add New Node,',newNode
                nodes.append(newNode)


    return 'fail'
    # test = [0,1,2]
    # print test[1:]

def valueOf(grid, yx):
    return grid[yx[1]][yx[2]]

def isNavigable(grid, nodes, yx):
    if(yx[1]<0 or yx[2]<0 or yx[2] >= len(grid[0]) or yx[1]>=len(grid)):
        return False

    return 0==valueOf(grid, yx) and not isInNodes(nodes, yx)

def isInNodes(nodes, yx):
    for n in nodes:
        if(yx[1]==n[1] and yx[2]==n[2]):
            return True

    return False

def isGoal(goaly, node):
    if(goaly[0]==node[1] and goaly[1]== node[2]):
        return True

    return False

def move(source, unitcost, step):
    return [source[0]+unitcost, source[1]+step[0], source[2]+step[1]]

print search(grid, init, goal, cost)
