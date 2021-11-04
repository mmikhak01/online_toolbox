import os
from django.shortcuts import render
from django.core import serializers


# views.py
import base64
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.models import User

from django.conf import settings
xml_dir = os.path.join(settings.BASE_DIR, 'static', 'xmls')




from django.views.decorators.cache import cache_control

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def wmst(request):
    if request.method == 'GET' and 'api_key' in request.GET:
        all_queries = request.GET['api_key']
        count_of_this = User.objects.filter(username=all_queries).count()
        if count_of_this > 0:
            return HttpResponse(open(os.path.join(xml_dir, 'all_wmst.xml')).read(), content_type='text/xml')
        else:
            pass


    return HttpResponse(open(os.path.join(xml_dir, 'free_wmst.xml')).read(), content_type='text/xml')
    #return HttpResponse('error')










def all2(request, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":

                    uname, passwd = base64.b64decode(auth[1]).split(b':')
                    uname, passwd = uname.decode(), passwd.decode()
                    print(uname, passwd)
                    print(request.user)
                    user = authenticate(username=uname, password=passwd)
                    if user is not None:
                        request.user = user
                        return HttpResponse('home')
                        #return render_to_response('pages/page.html', {"page": page})

        response = HttpResponse()
        response.status_code = 401
        response['WWW-Authenticate'] = 'Basic realm="%s"' % "Basci Auth Protected"
        return response


