from rest_framework import serializers
from .models import Task


class TaskSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['task_id','github_url','pr_number','github_token']
        read_only_fields = ['task_id']
