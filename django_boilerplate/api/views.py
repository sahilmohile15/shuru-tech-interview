from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# API View to store the matches information
class StoreMatchesView(APIView):
    def post(self, request):
        context = {}
        serializer_class = MatchesSerializer
        serializer = serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            context['status'] = status.HTTP_201_CREATED
            context['response_message'] = serializer.data
            
            return Response(context)
        
        context['status'] = status.HTTP_400_BAD_REQUEST
        context['response_message'] = "Invalid request"
        
        return Response(context)

# API view to retrieve matches by date
class RetrieveMatchByDateView(APIView):
    def get(self, request):
        context = {}
        serializer_class = MatchesSerializer
        mdate = request.GET.get('mdate', None)
        
        matches = Matches.objects.all().filter(date_of_match=mdate)
        
        serializer = serializer_class(data = matches,)
        
        if serializer.is_valid():
            context['status'] = status.HTTP_200_OK
            context['response_message'] = serializer.data
            
            return Response(context)
        
        context['status'] = status.HTTP_404_NOT_FOUND
        context['response_message'] = "Invalid request"
        
        return Response(context)
        