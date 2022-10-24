from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


from .models import *

class TodoList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        s = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(s,many=True)
        return Response(serializer.data)
    def post(self,request):
        todo = request.data
        serializer = TodoSerializer(data=todo)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response({"message":"not valid"})
    def delete(self,request,pk):
        s = Todo.object.get(id=pk)
        if s.user == request.user:
            s.delete()
            return Response({"message":"deleted"})
        return Response({"message":"Данное задание не является вашим!"})
    def put(self,request,pk):
        s = Todo.objects.get(id=pk)
        if s.user == request.user:
            serializer = TodoSerializer(s,request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Updated"})
        return Response(request.data)








class Todoget(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,pk):
        s = Todo.objects.get(id=pk)
        if s.user == request.user:
            serializer = TodoSerializer(s)
            return Response(serializer.data)
        return Response({"message":"not valid"})

