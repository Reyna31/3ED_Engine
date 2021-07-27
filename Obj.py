

class Obj(object):

    def __init__(self,filename):

        with open(filename,"r")as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.textcoords = []
        self.normals = []
        self.faces = []
        
        self.read()

    def read(self):
        for lines in self.lines:
            if lines:
                prefix, value =lines.split(' ', 1)

                if prefix == 'v':  #Vertices
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vt': #Texture Coords
                    self.textcoords.append(list(map(float, value.split(' '))))
                elif prefix == 'vn': #Normales
                    self.normals.append(list(map(float, value.split(' '))))
                elif prefix == 'f': #Faces
                    self.faces.append([list(map(int,face.split('/'))) for face in value.split(' ')])


