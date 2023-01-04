from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


# Create your views here.
class gamingAPI(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            query = Level.objects.get(id=pk)
            serialized = LevelSerializer(query)
            return Response(serialized.data)
        else:
            queryset = Level.objects.all()
            serialized = LevelSerializer(queryset, many=True)
            return Response(serialized.data)

    def post(self, request):
        serializedData = LevelSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response({'msg': 'data posted successfully'})
        else:
            return Response({'msg': 'something wrong'})

    def patch(self, request):
        pk = request.data.get("id", None)
        score = request.data.get("score", None)
        level = request.data.get("level", None)
        query = Level.objects.filter(id=pk).first()
        if int(score) > query.score and int(level) == query.level:
            query.score = int(score)
            query.save()
            return Response({'msg': 'score updated successfully'})
        elif int(level) > query.level:
            serializedData = LevelSerializer(query, data=request.data)
            serializedData.is_valid()
            serializedData.save()
            return Response({'msg': 'level updated successfully'})
        else:
            return Response({'msg': 'cannot be update'})

    def delete(self, request):
        pk = request.data.get("id", None)
        query = Level.objects.filter(id=pk).first()
        query.delete()
        return Response({'msg': 'Deleted successfully'})


