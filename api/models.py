from django.db import models

class Task(models.Model):
    task_id = models.UUIDField(blank=True,null=True)
    github_url = models.URLField()
    pr_number = models.IntegerField()
    github_token = models.CharField(max_length=650,blank=True,null=True)

