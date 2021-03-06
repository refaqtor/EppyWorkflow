from eppy import modeleditor
from eppy.modeleditor import IDF

# Context: Design assistance projects.
# Function: Assign construction of ground contact surfaces.
# Arg. Values: 
#				- Surface Type: Wall, Roof, Floor.
#				- Construction: Any construction available in the model that matches the above specification.

def AssignGroundContactSurfacesConstruction(idf_file,*args):
	BuildingSurfaceObjects = idf_file.idfobjects["BUILDINGSURFACE:DETAILED"]
	SurfaceType = args[0][0]
	ConstructionName = args[0][1]	
	
	for i in range(0,len(BuildingSurfaceObjects)):
		if BuildingSurfaceObjects[i].Outside_Boundary_Condition == "Ground" and BuildingSurfaceObjects[i].Surface_Type == SurfaceType:
			BuildingSurfaceObjects[i].Construction_Name = ConstructionName

if __name__ == '__main':
	AssignGroundContactSurfacesConstruction(idf_file,SurfaceType,ConstructionName)