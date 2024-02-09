from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import BloodDoner 
from.serializers import BloodDonerSerializers

# Create your views here.
@api_view(['GET','POST'])
def blood_doner(request):
    if request.method == 'GET':
        doners = BloodDoner.objects.all().order_by('id')
        serializer=BloodDonerSerializers(doners,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=BloodDonerSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Success':"Successfully created"})

@api_view(['GET','POST'])
def blood_doner_update(request,id):
    if request.method == 'GET':
        doners = BloodDoner.objects.get(id=id)
        serializer=BloodDonerSerializers(doners,many=False)
        return Response(serializer.data)
    
    if request.method=='POST':
        doners = BloodDoner.objects.get(id=id)
        serializer=BloodDonerSerializers(data=request.data,instance=doners)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Success':"Successfully Updated"})  

@api_view(['delete'])
def blood_doner_delete(request,id):
    
    doners = BloodDoner.objects.get(id=id)
    doners.delete()

    return Response({'Success':"Successfully deleted"})         

# @api_view(['GET'])
# def hello_world(request):
#     return Response({"message": "Hello, world!"})