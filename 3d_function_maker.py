import numpy as np
import math

# density of vertices in the fucntion
density = 4.0

# scale of the fucntion being converted to an object
scale = 1

# overall size of the 3D object
size = 20

# offset from the corner of the object to the origin
offset = 10

# the thickness of the 3D object
width = 0.1

# calculate function
def function(x, y):
    return 0.5*math.sin(x) + 0.5*math.sin(y)

# (x, y, z, top y index, bottom y index)
points = np.zeros((math.floor(density * size), math.floor(density * size), 5))

# string to be saved to the .obj file
file_content = ""

# generate function vertices
k = 1
size + 1.1/density 

# top points
for i in range(math.floor(density * size)):
    for j in range(math.floor(density * size)):
        points[i][j][0] = (i/density) - offset
        points[i][j][1] = function(i/density - offset, j/density - offset)
        points[i][j][2] = (j/density) - offset
        points[i][j][3] = k
        k += 1
        file_content += "v " + str(points[i][j][0]) + " " + str(points[i][j][1]) + " " + str(points[i][j][2]) + "\n"
    
# bottom points
for i in range(math.floor(density * size)):
    for j in range(math.floor(density * size)):
        points[i][j][4] = k
        k += 1
        file_content += "v " + str(points[i][j][0]) + " " + str(points[i][j][1] - width) + " " + str(points[i][j][2]) + "\n"
  
# generate function faces
for i in range(math.floor(density * size)):
    for j in range(math.floor(density * size)):
        if i == 0:
            if j > 0:
                file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i][j-1][3])) + " " + str(int(points[i][j][4])) + "\n"
            if j < math.floor(density * size) - 1:
                file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i][j][4])) + " " + str(int(points[i][j+1][4])) + "\n"
                
        if i == math.floor(density * size) - 1:
            if j > 0:
                file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i][j][4])) + " " + str(int(points[i][j-1][3])) + "\n"
            if j < math.floor(density * size) - 1:
                file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i][j+1][4]))  + " " + str(int(points[i][j][4])) + "\n"
                
        if j == 0:
            if i > 0:
                file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i][j][4])) + " " + str(int(points[i-1][j][3])) + "\n"
            if i < math.floor(density * size) - 1:
                file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i+1][j][4])) + " " + str(int(points[i][j][4])) + "\n"
                
        if j == math.floor(density * size) - 1:
            if i > 0:
                file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i-1][j][3])) + " " + str(int(points[i][j][4])) + "\n"
            if i < math.floor(density * size) - 1:
                file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i][j][4]))  + " " + str(int(points[i+1][j][4])) + "\n"
                      
        if i > 0 and j > 0:
             file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i][j-1][3])) + " " + str(int(points[i-1][j][3])) + "\n"
             file_content += "f " + str(int(points[i][j][4])) + " " + str(int(points[i-1][j][4])) + " " + str(int(points[i][j-1][4])) + "\n"          
 
        if i < math.floor(density * size) - 1 and j < math.floor(density * size) - 1:
             file_content += "f " + str(int(points[i][j][3])) + " " + str(int(points[i][j+1][3])) + " " + str(int(points[i+1][j][3])) + "\n"
             file_content += "f " + str(int(points[i][j][4])) + " " + str(int(points[i+1][j][4])) + " " + str(int(points[i][j+1][4])) + "\n"
        
    
with open('shape.obj', 'w') as f:
    f.write(file_content)