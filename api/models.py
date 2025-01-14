from django.db import models

class AnalyzePRRequest(models.Model):
    github_url = models.URLField()
    pr_number = models.IntegerField()
    github_token = models.CharField(max_length=650,blank=True,null=True)

