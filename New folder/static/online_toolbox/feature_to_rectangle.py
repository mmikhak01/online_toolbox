import arcpy,os
inFC = arcpy.GetParameterAsText(0)
outFC = arcpy.GetParameterAsText(1)

outPath, outName = os.path.split(outFC)
fcDesc = arcpy.Describe(inFC)
inshapetype = fcDesc.shapetype
if inshapetype == "Point" or inshapetype == "Multipoint":
	arcpy.AddError("point feature can't converte to rectangle")
else:
	if arcpy.Exists(outFC):
	    arcpy.Delete_management(outFC)
	arcpy.CreateFeatureclass_management(outPath, outName, "Polygon", "", "DISABLED", "DISABLED", inFC)
	myxmin = []
	myxmax = []
	myymin = []
	myymax = []
	ms = 0
	for row in arcpy.da.SearchCursor(inFC, ["SHAPE@"]):
	    extent = row[0].extent
	    myxmin.append(extent.XMin)
	    myxmax.append(extent.XMax)
	    myymin.append(extent.YMin)
	    myymax.append(extent.YMax)
	    ms+=1
	    array = arcpy.Array([arcpy.Point(extent.XMin, extent.YMin),
	                     arcpy.Point(extent.XMin, extent.YMax),
	                     arcpy.Point(extent.XMax, extent.YMax),
	                     arcpy.Point(extent.XMax, extent.YMin)])
	    Polygon = arcpy.Polygon(array)
	    cursor = arcpy.da.InsertCursor(outFC, ("SHAPE@"))
	    cursor.insertRow((Polygon,))
	    del cursor