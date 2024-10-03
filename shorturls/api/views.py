from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from main.models import Urlsshort
import json  
import string
import random

@api_view(['GET', 'POST'])
def getData(request):
    dictTest = {'data': ""}
    if request.method == 'POST':
        data = request.data
        domain = request.build_absolute_uri('/')[:-1]
        res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=10))
        shortLink = domain + "/" + res
        newRecord = Urlsshort.objects.create(link=res, url=data['data'])
        dictTest['data'] = shortLink
        json_object = json.dumps(dictTest, indent = 4)
        
    return Response(dictTest)