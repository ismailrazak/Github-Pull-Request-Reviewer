import requests
import base64


def extract_content_from_pr(url,pr_no,token=None):
    headers = {'Authorization':token} if token else {}
    project = url.split('/')[-1]
    owner = url.split('/')[-2]
    pr_response = requests.get(f"https://api.github.com/repos/{owner}/{project}/pulls/{pr_no}/files",headers=headers)
    pr_response.raise_for_status()
    filename = pr_response.json()[0].get('filename')
    content_response = requests.get(f"https://api.github.com/repos/{owner}/{project}/contents/{filename}",headers=headers)
    content_response.raise_for_status()
    content_base64  = content_response.json().get('content')
    content = base64.b64decode(content_base64).decode()
    return content