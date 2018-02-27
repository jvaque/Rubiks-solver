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
    
    def storeFace(self, face):
        #Copies over the face selected to the temporal array
        for i in range(3):
            for j in range(3):
                self.rotatedFace[0][i][j] = self.cube[face][i][j]
    
    def rotateFace(self, face):
        #Makes propper rotation of the cube face
        for i in range(3):
            k = 2
            for j in range(3):
                self.cube[face][i][j] = self.rotatedFace[0][k][i]
                k -= 1
    
    def storeEdgesWY(self, face):
        #If statement just so I dont make stupid mistakes
        #Note to future me to remove or have a better system
        if face == 0:
            for i in range(4):
                for j in range(3):
                    position = i+1
                    self.rotatedFace[1][i][j] = self.cube[position][0][j]
        elif face == 5:
            for i in range(4):
                for j in range(3):
                    if i <= 1:
                        position = i+3
                    else:
                        position = i-1
                    self.rotatedFace[1][i][j] = self.cube[position][2][j]
        else:
            print("ERROR!!!!!!!")
    
    def rotateEdgesWY(self, face):
        #If statement just so I dont make stupid mistakes
        #Note to future me to remove or have a better system
        if face == 0:
            column = 0
        elif face == 5:
            column = 2
        else:
            print("ERROR!!!!!!!")
        
        for i in range(4):
            for j in range(3):
                if i == 3:
                    self.cube[4][column][j] = self.rotatedFace[1][0][j]
                else:
                    self.cube[i+1][column][j] = self.rotatedFace[1][i+1][j]
    
    def rotateWhite(self):
        #Store
        self.storeFace(0)
        self.storeEdgesWY(0)
        
        #Move
        self.rotateFace(0)
        self.rotateEdgesWY(0)
        
        self.clearRotatedFace()
    
    def rotateYellow(self):
        #Store
        self.storeFace(5)
        self.storeEdgesWY(5)
        
        #Move
        self.rotateFace(5)
        self.rotateEdgesWY(5)
        
        self.clearRotatedFace()
    

#Just for testing purposes
def main():
    testCube = PyCube()
    testCube.show()
    testCube.rotateWhite()
    testCube.show()
    testCube.rotateYellow()
    testCube.show()

main()