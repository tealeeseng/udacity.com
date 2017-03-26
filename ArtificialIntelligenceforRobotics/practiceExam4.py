#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.
#practice exam 4, still not correct. [0.03448275862068965, 0.03448275862068965, 0.03448275862068965, 0.31034482758620685, 0.31034482758620685]

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'green', 'red', 'green', 'red']
measurements = ['red', 'red']
motions = [1,1]
pHit = 0.9
pMiss = 0.1
pExact = 1.0
pOvershoot = 0.0
pUndershoot = 0.0

# make sense and move methods capable of 2D computing. start with simply model.
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        l = i-U
        if l<0:
            l=0
        s = pExact * p[l]
        # s = s + pOvershoot * p[(i-U-1) % len(p)]
        # s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q
#
# ADD CODE HERE
#
for i in range(len(measurements)):
    p=move(sense(p,measurements[i]),motions[i])
print p         
