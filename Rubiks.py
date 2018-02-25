import pprint

class PyCube:
    def __init__(self):
        cube = [[[0 for k in range(3)] for j in range(3)] for i in range(6)]
        colours = ['W', 'O', 'G' , 'R', 'B', 'Y']
        color = 0
    
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    cube[i][j][k] = colours[color]
            color += 1
    
    def show(self):
        pprint.pprint(self.cube)

#Just for testing purposes
def main():
    testCube = PyCube()
    testCube.show()