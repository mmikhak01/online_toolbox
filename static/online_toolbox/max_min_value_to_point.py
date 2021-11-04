
import arcpy,os
from arcpy import env
from arcpy.sa import *
inRaster = arcpy.GetParameterAsText(0)
workspace = arcpy.GetParameterAsText(1)

env.workspace = os.path.dirname(inRaster)





def raster_Statistics_is_OK(myraster, what = "MINIMUM"):
	myraster_= arcpy.Describe(myraster)
	myraster = myraster_.catalogPath

	try:
		raster_st = arcpy.GetRasterProperties_management(myraster, what)
		return True
	except arcpy.ExecuteError:
		msgs = arcpy.GetMessages(2)
        	error_code = str(msgs).replace(":","").split(" ")[1]
		if error_code == "001100":
			return False
	return 'Another problem'

def calc_raster_stat(myraster):
	arcpy.CalculateStatistics_management(myraster, "1", "1", "", "OVERWRITE", "")

def getstat(myraster,what = "MINIMUM"):
	mdic = {'min':"MINIMUM", 'max':"MAXIMUM", 'std':"STD", 'mean':"MEAN"}
	if what.lower() in mdic.keys():
           what = mdic[what.lower()]
	myraster_= arcpy.Describe(myraster)
	myraster = myraster_.catalogPath
	stat_isok = raster_Statistics_is_OK(myraster, what = "MINIMUM")
	if stat_isok != True:
		calc_raster_stat(myraster)
getstat(inRaster,what = "MINIMUM")



for www in ["MINIMUM","MAXIMUM"]:
	mmmVal = arcpy.GetRasterProperties_management(inRaster,www).getOutput(0)
	outCon = Con(Raster(inRaster) == float(mmmVal),1, 0)

	outSetNull = SetNull(outCon, 1, "VALUE <> 1")
	baseName = arcpy.Describe(inRaster).baseName
	outPoint = workspace +'/'+ baseName + '_' + www + '.shp'
	field = "VALUE"
	arcpy.RasterToPoint_conversion(outSetNull, outPoint, field)
