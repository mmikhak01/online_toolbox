
import arcpy, os
arcpy.env.overwriteOutput = True
from arcpy.sa import *




def field2list(infc,field):
	list = []
	for row in arcpy.da.SearchCursor(infc, [field]):
		list.append(row[0])
	return list




infc = arcpy.GetParameterAsText(0)
field = arcpy.GetParameterAsText(1)
workspace = arcpy.GetParameterAsText(2)


fields = arcpy.ListFields(infc)
for mfield in fields:
	if mfield.name == field:
			ftype = mfield.type
			break


alls = field2list(infc,field)
unique = list(set(alls))
arcpy.AddMessage(unique)

for xx in unique:
	if ftype == "String":
		myexp = "\"%s\" = '%s'"%(field,xx)
	else:
		myexp = "\"%s\" = %s"%(field,xx)

	#nameee = str(xx)
	nameee = xx
	ddd = "-()[]{}/\\*"
	for rrr in ddd:
		nameee =nameee.replace(rrr,"_")
	arcpy.Select_analysis(infc, workspace + "/" + nameee, myexp)

	#arcpy.Select_analysis(infc, workspace + "/" + str(xx), "\"%s\" =  %s"%(field,xx))
