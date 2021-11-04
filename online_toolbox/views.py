from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf import settings
import os

from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse

@csrf_exempt
def download_file(request):

    if request.method == 'POST':
        filename = request.POST.get('filename')
        file_path = os.path.abspath(os.path.join(settings.BASE_DIR, f"static/online_toolbox/files/{filename}"))
        print(file_path)
        if os.path.exists(file_path):
            file = open(file_path, 'rb')
            response = FileResponse(file)
            return response

    text = """Get method"""
    return HttpResponse(text)



@csrf_exempt
def index(request):



    if request.method == 'POST':
        uid = request.POST.get('uid')
        script_name = request.POST.get('script_name')



        script_path = os.path.abspath(os.path.join(settings.BASE_DIR, f"static/online_toolbox/{script_name}.py"))
        print(script_path)
        if not os.path.exists(script_path):

            text = """
        import arcpy
        arcpy.AddMessage("Toolbox is not a valid tool")
           """

        else:
            with open(script_path, 'r', encoding='utf-8') as fff:
                text = fff.read()



        response = HttpResponse(text)
        response['Content-Type'] = "text/plain"
        #response["Access-Control-Allow-Methods"] = "GET,POST, OPTIONS"
        response["Access-Control-Allow-Methods"] = "*"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        response["Access-Control-Allow-Origin"] = "*"

        return response

    text = """Get method mmm"""
    return HttpResponse(text)

