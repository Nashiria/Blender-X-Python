try:
    import bpy
except:
    pass
#--------------------------------------------------------------------------
# Default Commands
#--------------------------------------------------------------------------
def createMesh(meshName,meshData):
    mesh=bpy.data.meshes.new(meshName)
    mesh.from_pydata(meshData[0],meshData[1],meshData[2])
    mesh.update()
    return mesh
def createObject(mesh,objectName):
    mesh.update()
    object=bpy.data.objects.new(objectName,mesh)
    return object
def collectObject(object):
    view_layer=bpy.context.view_layer
    view_layer.active_layer_collection.collection.objects.link(object)

#--------------------------------------------------------------------------
# Object Commands
# --------------------------------------------------------------------------


# Rectangle Commands
def rectangleData(translationXYZ,scaleXYZ):
    vertices = [(scaleXYZ[0]+translationXYZ[0],scaleXYZ[1]+translationXYZ[1],-scaleXYZ[2]+translationXYZ[2]),
                (scaleXYZ[0]+translationXYZ[0], -scaleXYZ[1]+translationXYZ[1],-scaleXYZ[2]+translationXYZ[2]),
                (-scaleXYZ[0]+translationXYZ[0],-scaleXYZ[1]+translationXYZ[1],-scaleXYZ[2]+translationXYZ[2]),
                (-scaleXYZ[0]+translationXYZ[0],scaleXYZ[1]+translationXYZ[1],-scaleXYZ[2]+translationXYZ[2]),
                (scaleXYZ[0]+translationXYZ[0], scaleXYZ[1]+translationXYZ[1],scaleXYZ[2]+translationXYZ[2]),
                (scaleXYZ[0]+translationXYZ[0],-scaleXYZ[1]+translationXYZ[1],scaleXYZ[2]+translationXYZ[2]),
                (-scaleXYZ[0]+translationXYZ[0],-scaleXYZ[1]+translationXYZ[1], scaleXYZ[2]+translationXYZ[2]),
                (-scaleXYZ[0]+translationXYZ[0], scaleXYZ[1]+translationXYZ[1],scaleXYZ[2]+translationXYZ[2])]
    edges = []
    faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 7, 3), (0, 1, 5, 4), (1, 2, 6, 5), (7, 6, 2, 3)]
    return (vertices,edges,faces)
def createRectangle(translationXYZ=(0,0,0),scaleXYZ=(1,1,1),meshName="New Mesh",objectName="New Object"):
    collectObject(createObject(createMesh(meshName,rectangleData(translationXYZ,scaleXYZ)),objectName))

# Procedural Generation Commands
def createRandomCubes(cubeSize=(1,1,1),cubeCount=20):
    translations=[]
    count=0
    import random
    for x in range(cubeCount):
        for y in range(cubeCount):
            translations.append((0+x*cubeSize[0]*2,0+y*cubeSize[1]*2,random.randint(-5,5)/10))
            createRectangle(translations[count],cubeSize,"Cube"+str(count)+" Mesh","Cube"+str(count)+" Object")
            count+=1
def createRandomCubesWithSpaces(cubeSize=(1,1,1),cubeCount=20,minSpace=0,maxSpace=5):
    translations=[]
    count=0
    import random
    yS=[]
    lastY=0
    for x in range(cubeCount):
        lastX = lastY
        lastY = 0
        for y in range(cubeCount):
                lastY = lastY + cubeSize[0]*2 + random.randint(minSpace * 10, maxSpace * 10) / 10
                translations.append((lastX,lastY,random.randint(-5,5)/10))
                print(translations[len(translations)-1])
        lastY=translations[x][1]
    for translation in translations:
        createRectangle(translation, cubeSize, "Cube" + str(count) + " Mesh", "Cube" + str(count) + " Object")

