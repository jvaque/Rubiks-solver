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
        # for i in range(6):
        #     counter = 10 * (i+1)
        #     for j in range(3):
        #         for k in range(3):
        #             self.cube[i][j][k] = counter
        #             counter += 1
        #delete between coments

    def show(self):
        print()
        pprint.pprint(self.cube)
        # for debugging
        # print()
        # pprint.pprint(self.rotatedFace)
    
    def clearRotatedFace(self):
        for i in range(2):
            for j in range(3+i):
                for k in range(3):
                    self.rotatedFace[i][j][k] = ''
    
    def rotateFace(self, face):
        #Makes propper rotation of the cube face
        for i in range(3):
            k = 2
            for j in range(3):
                self.cube[face][i][j] = self.rotatedFace[0][k][i]
                k -= 1
    
    def storeFace(self, face):
        #Copies over the face selected to the temporal array
        for i in range(3):
            for j in range(3):
                self.rotatedFace[0][i][j] = self.cube[face][i][j]
    
    def rotateWhite(self):
        #Copying over face
        self.storeFace(0)
        
        #copying over the connected edges
        for i in range(4):
            for j in range(3):
                self.rotatedFace[1][i][j] = self.cube[i+1][0][j]
        
        #move things
        self.rotateFace(0)
        
        for i in range(4):
            for j in range(3):
                if i == 3:
                    self.cube[4][0][j] = self.rotatedFace[1][0][j]
                else:
                    self.cube[i+1][0][j] = self.rotatedFace[1][i+1][j]
        
        self.clearRotatedFace()
    
    def rotateYellow(self):
        #Copying over face
        self.storeFace(5)
        
        #copying over the connected edges
        for i in range(4):
            for j in range(3):
                self.rotatedFace[1][i][j] = self.cube[i+1][2][j]
        
        #move things
        self.rotateFace(5)
        
        for i in range(4):
            for j in range(3):
                if i == 0:
                    self.cube[1][2][j] = self.rotatedFace[1][3][j]
                else:
                    self.cube[i+1][2][j] = self.rotatedFace[1][i-1][j]
        
        self.clearRotatedFace()
    

#Just for testing purposes
def main():
    testCube = PyCube()
    testCube.show()
    testCube.rotateWhite()
    testCube.rotateYellow()
    testCube.show()

main()