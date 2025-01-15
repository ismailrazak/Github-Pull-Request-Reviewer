from rest_framework.views import APIView,Response
from rest_framework import status
from celery.result import AsyncResult
from uuid import uuid4
from .tasks import analyze_pr_task


class StartTaskView(APIView):
    def post(self,request,pk=None):
        try:
            url = request.data['github_url']
            pr_no = request.data['pr_number']
            token  =request.data['github_token']
            task_id = str(uuid4())
            result = analyze_pr_task.apply_async(
    args=[url, pr_no, task_id, token],
    task_id=task_id
)
            return Response({'task_id':task_id,'status':"STARTED"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':f'{e}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckTaskView(APIView):
    def get(self,request,task_id,pk=None):
            task_id = task_id
            result=AsyncResult(task_id)
            return Response(
                {'task_id':task_id,'status':result.state,'result':result.result}
            )














#todo : check if pr_no exists and return appropriate response.
#todo : also check async result in the end if it works properly.


