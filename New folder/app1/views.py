from django.shortcuts import render
from django.shortcuts import HttpResponse


def index2(request):
    context = {'dams':1}
    return render(request, 'index.html', context)

def index22(request):
   text = """
import arcpy   
arcpy.AddMessage(parameters[0].valueAsText)
   """
   return HttpResponse(text)




from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def index(request):


    text = """
import arcpy   
arcpy.AddMessage(arcpy.GetParameterAsText(0))
   """

    response = HttpResponse(text)
    response['Content-Type'] = "text/plain"
    #response["Access-Control-Allow-Methods"] = "GET,POST, OPTIONS"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    response["Access-Control-Allow-Origin"] = "*"

    return response


