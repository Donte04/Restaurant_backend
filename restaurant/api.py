# define endpoints here + add url in urls.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Plat
from .serializers import PlatSerializer

#decorator : positioned above a function, it is used to describe its functionality in someway

@api_view(['GET','POST'])
def les_plats(request, format=None):
    if request.method == 'GET':
        #get all the plat
        plats = Plat.objects.all()
        #serialize them
        serializer = PlatSerializer(plats, many=True)
        #return json
        return Response(serializer.data) 

    if request.method == 'POST':
        serializer = PlatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_CREATED)

@api_view(['GET','PUT','DELETE'])
def par_plat(request, id, format=None):
    
    try:
        plat = Plat.objects.get(pk=id) #pk: primary key
    except Plat.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
       serializer = PlatSerializer(plat)
       return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PlatSerializer(plat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        plat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
