from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import SelfUser
from .serializer import SelfUserSerializer

@api_view(['GET'])
def allUsers(request):
    users = SelfUser.objects.all()
    serializer = SelfUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = SelfUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def userDetail(request,pk):
    try:
        user = SelfUser.objects.get(pk=pk)
    except SelfUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SelfUserSerializer(user)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = SelfUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
