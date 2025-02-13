import base64
import json
from uuid import uuid4

import requests

from .ai_agent import analyze_content_with_llm


def extract_content_from_pr(url, pr_no, token=None):
    # try:
    headers = {"Authorization": token} if token else {}
    project = url.split("/")[-1]
    owner = url.split("/")[-2]
    pr_response = requests.get(
        f"https://api.github.com/repos/{owner}/{project}/pulls/{pr_no}/files",
        headers=headers,
    )
    pr_response.raise_for_status()
    pr_repsonses = pr_response.json()
    content_list = []
    for pr_response in pr_repsonses:
        filename = pr_response.get("filename")
        content_response = requests.get(
            f"https://api.github.com/repos/{owner}/{project}/contents/{filename}",
            headers=headers,
        )
        content_response.raise_for_status()
        content_base64 = content_response.json().get("content")
        content = base64.b64decode(content_base64).decode()
        content_list.append(content)
    return content_list


# except requests.exceptions.HTTPError:
#     return []


def analyze_pr(url, pr_no, task_id, token=None):
    response_list = []
    try:
        content_list = extract_content_from_pr(url, pr_no, token)
        if not content_list:
            return {"HTTP Error": "There was a issue in the request."}
        for content in content_list:
            results = analyze_content_with_llm(content)
            if not results:
                return {"error": "Files are too large too process for LLM."}
            results = json.loads(results)
            response_list.append(results)
        return {"task_id": task_id, "results": response_list}
    except Exception as e:
        return {"task_id": task_id, "error": content_list}


# todo
