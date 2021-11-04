import arcpy,os
arcpy.CheckOutExtension("spatial")
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True

inrasters = arcpy.GetParameterAsText(0)
target = arcpy.GetParameterAsText(1)
if float(target)%1 == 0:
    target = int(target)
else:
    target = float(target)
    
workspace = arcpy.GetParameterAsText(2)


pole = inrasters.split(";")
for inraster in pole:
	inraster = Raster(inraster)
	myshp= arcpy.Describe(inraster)
	rname = myshp.baseName

	xxx = Con(IsNull(inraster),target,inraster)
	xxx.save(workspace + "//" + rname)
