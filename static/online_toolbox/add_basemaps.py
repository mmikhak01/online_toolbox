import arcpy,time

arcpy.env.overwriteOutput = True
map_name = arcpy.GetParameterAsText(0)

import os
script_path = os.path.dirname(__file__)

import requests
from io import BytesIO

### url ='http://127.0.0.1:8000/online_toolbox/download_file'
### we get url globaly from arcmap script
url = '/'.join(s.strip('/') for s in [url , "/download_file"])

data = {
  'filename': str(map_name) + '.lyr',
}

response = requests.post(url, data=data, stream=True)

import shutil
out_p = os.path.join(script_path, 'local_filename.lyr')
with open(out_p, 'wb') as f:
        shutil.copyfileobj(response.raw, f)

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]  

layer = arcpy.mapping.Layer(out_p)   
arcpy.mapping.AddLayer(df, layer, "BOTTOM")  

  
arcpy.RefreshTOC()  
arcpy.RefreshActiveView()  