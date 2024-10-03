from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from main.models import Urlsshort

@api_view(['GET', 'POST'])
def getData(request):
    dictTest = {'records': 0, 'fetched': 0, 'message': 0}
    if request.method == 'POST':
        data = request.data
        newRecord = Urlsshort.objects.create(link="/rafael", url=data['data'])
        print(data)
        dictTest['records'] = "Hello world"
        print("Record at the db = ", newRecord)
        
    return Response(dictTest)