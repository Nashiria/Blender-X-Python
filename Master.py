import bpy

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
def createRectangle(translationXYZ,scaleXYZ,meshName,objectName):
    collectObject(createObject(createMesh(meshName,rectangleData(translationXYZ,scaleXYZ)),objectName))


createRectangle((0,0,0),(2,2,2),"Test Mesh","Test Object")
