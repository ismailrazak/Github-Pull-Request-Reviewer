from django.shortcuts import render
from rest_framework.views import APIView,Response
from .serializers import AnalyzerPrRequestSerialzier
from .models import AnalyzePRRequest
from rest_framework import status

class EntryView(APIView):
    def post(self,request,pk=None):
        try:
            serializer = AnalyzerPrRequestSerialzier(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':f'{e}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
