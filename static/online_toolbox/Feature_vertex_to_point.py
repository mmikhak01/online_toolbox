import arcpy, os
import pythonmood
inFC = arcpy.GetParameterAsText(0)
outFC = arcpy.GetParameterAsText(1)
#distance = float(arcpy.GetParameterAsText(1))

outPath, outName = os.path.split(outFC)


if arcpy.Exists(outFC):
	arcpy.Delete_management(outFC)
outFC = arcpy.CreateFeatureclass_management(outPath, outName, "POINT", "", "DISABLED", "DISABLED", inFC)

pythonmood.my_addfield(outFC, 'x', type="n")
pythonmood.my_addfield(outFC, 'y', type="n")

allpoints = []
for row in arcpy.da.SearchCursor(inFC, ["OID@", "SHAPE@"]):
    for part in row[1]:
        for vertex in part:
            if [vertex.X, vertex.Y] not in allpoints:
	        point = arcpy.Multipoint(arcpy.Array(arcpy.Point(vertex.X, vertex.Y)))
	        point = arcpy.Point(vertex.X, vertex.Y)
     	        cursor = arcpy.da.InsertCursor(outFC, ["SHAPE@", 'x', 'y'])
    	        cursor.insertRow((point,vertex.X,vertex.Y))
		allpoints.append([vertex.X, vertex.Y])
		arcpy.AddMessage([vertex.X, vertex.Y])



