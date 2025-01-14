from celery import shared_task
from utils.github import analyze_pr

@shared_task()
def analyze_pr_task(url,pr_no,token=None):
    result = analyze_pr(url,pr_no,token)
    return result