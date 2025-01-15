from rest_framework import serializers


class StartTaskSerializer(serializers.Serializer):
    url = serializers.URLField()
    pr_no = serializers.IntegerField()
    token = serializers.CharField(max_length=400, allow_blank=True, allow_null=True)
    task_id = serializers.UUIDField()
