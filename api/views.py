from django.shortcuts import render
from rest_framework.views import APIView,Response
from .serializers import TaskSerialzier
from .models import Task
from rest_framework import status
from tasks import analyze_pr
from celery.result import AsyncResult
from uuid import uuid4


class StartTaskView(APIView):
    def post(self,request,pk=None):
        try:
            url = request.data['github_url']
            pr_no = request.data['pr_number']
            token  =request.data['github_token']
            task_id = str(uuid4())
            result = analyze_pr(url, pr_no,task_id, token)
            serializer = TaskSerialzier(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(task_id=task_id)
            return Response(data={'task_id':task_id,'status':"CREATED",'github_url':url,'pr_number':pr_no,"github_token":token},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':f'{e}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckTaskView(APIView):
    def post(self,request,pk=None):
        task_id = request.data['task_id']

        if Task.objects.filter(task_id=task_id).exists():
            result=AsyncResult(task_id)
            return Response(
                {'task_id':task_id,'status':result.state}
            )















#todo : check if pr_no exists and return appropriate response.
#todo : also check async result in the end if it works properly.


