import pprint

cube = [[[0 for k in range(3)] for j in range(3)] for i in range(6)]
colours = ['W', 'O', 'G' , 'R', 'B', 'Y']
color = 0

pprint.pprint(cube)

for i in range(6):
    for j in range(3):
        for k in range(3):
            cube[i][j][k] = colours[color]
    color += 1

pprint.pprint(cube)