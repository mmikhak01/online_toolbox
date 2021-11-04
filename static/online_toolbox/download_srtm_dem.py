import arcpy,time

arcpy.env.overwriteOutput = True
feature_class = arcpy.GetParameterAsText(0)
dem_source = arcpy.GetParameterAsText(1)
out_tif = arcpy.GetParameterAsText(2)






def get_Extent_in_DD(feature_class):
    E = None
    N = None
    W = None
    S = None
    sp4 = arcpy.SpatialReference(4326)
    for row in arcpy.da.SearchCursor(feature_class, ["SHAPE@"], spatial_reference=sp4):
        extent = row[0].extent
##        print("XMin: {0}, YMin: {1}".format(extent.XMin, extent.YMin))
##        print("XMax: {0}, YMax: {1}".format(extent.XMax, extent.YMax))

        if (E == None) or (E < extent.XMax):
            E = extent.XMax
        if (W == None) or (W > extent.XMin):
            W = extent.XMin
        if (N == None) or (N < extent.YMax):
            N = extent.YMax
        if (S == None) or (S > extent.YMin):
            S = extent.YMin
    return {'E':E,'N':N,'W':W,'S':S}



def download(url, path):
    import urllib
    import sys

    if sys.version_info[0] >= 3:
        from urllib.request import urlretrieve
    else:
        from urllib import urlretrieve

    urlretrieve(url, path)


DEFAULT_DEM_SERVER = {
	"SRTM_30m" : ["https://portal.opentopography.org/API/globaldem?demtype=SRTMGL1&west={W}&east={E}&south={S}&north={N}&outputFormat=GTiff", 'OpenTopography SRTM 30m', 'OpenTopography.org web service for SRTM 30m global DEM'],
	"SRTM_90m" : ["https://portal.opentopography.org/API/globaldem?demtype=SRTMGL3&west={W}&east={E}&south={S}&north={N}&outputFormat=GTiff", 'OpenTopography SRTM 90m', 'OpenTopography.org web service for SRTM 90m global DEM'],
	"GMRT" : ["http://www.gmrt.org/services/GridServer?west={W}&east={E}&south={S}&north={N}&layer=topo&format=geotiff&resolution=high", 'Marine-geo.org GMRT', 'Marine-geo.org web service for GMRT global DEM (terrestrial (ASTER) and bathymetry)']
}



extent = get_Extent_in_DD(feature_class)


dem30_url = DEFAULT_DEM_SERVER[dem_source][0].format(E=extent['E'], N=extent['N'], S=extent['S'], W=extent['W'])
download(dem30_url, out_tif)


def calc_raster_stat(myraster):
	arcpy.CalculateStatistics_management(myraster, "1", "1", "", "OVERWRITE", "")
try:
    calc_raster_stat(out_tif)
except:
    pass