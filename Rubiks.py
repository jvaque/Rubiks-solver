import pprint

n = 3
cube = [[[0 for k in range(n)] for j in range(n)] for i in range(n-1)]
colours = ['W', 'Y', 'R' , 'B', 'G', 'O']
color = 0

for i in range(n-1):
    for j in range(n):
            for k in range(n):
                cube[i][j][k] = colours[color]
            color += 1

pprint.pprint(cube)