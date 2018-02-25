import pprint

class PyCube:
    def __init__(self):
        self.cube = [[['' for k in range(3)] for j in range(3)] for i in range(6)]
        self.rotatedFace = [[['' for k in range(3)] for j in range(3)], [['' for k in range(3)] for j in range(4)]]
        colours = ['W', 'O', 'G', 'R', 'B', 'Y']
        color = 0
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    self.cube[i][j][k] = colours[color]
            color += 1
        
        #for testing
        # counter = 10
        # for i in range(6):
        #     for j in range(3):
        #         for k in range(3):
        #             self.cube[i][j][k] = counter
        #             counter += 1
        #delete between coments

    def show(self):
        print()
        pprint.pprint(self.cube)
        print()
        pprint.pprint(self.rotatedFace)
    
    def clearRotatedFace(self):
        for i in range(2):
            for j in range(3+i):
                for k in range(3):
                    self.rotatedFace[i][j][k] = ''
    
    def rotateWhite(self):
        #Copying over face
        for i in range(3):
            for j in range(3):
                self.rotatedFace[0][i][j] = self.cube[0][i][j]
        #copying over the connected edges
        for i in range(4):
            for j in range(3):
                self.rotatedFace[1][i][j] = self.cube[i+1][0][j]
        
        #move things
        for i in range(3):
            k = 2
            for j in range(3):
                self.cube[0][i][j] = self.rotatedFace[0][k][i]
                k -= 1
        
        for i in range(4):
            for j in range(3):
                if i == 3:
                    self.cube[i+1][0][j] = self.rotatedFace[1][0][j]
                else:
                    self.cube[i+1][0][j] = self.rotatedFace[1][i+1][j]
        
        self.clearRotatedFace()
    
    

#Just for testing purposes
def main():
    testCube = PyCube()
    testCube.show()
    testCube.rotateWhite()
    testCube.show()

main()