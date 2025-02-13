# GitHub PR Review Checker

## Live Link:
https://github-pull-request-reviewer.onrender.com/api/start_task/

This is a RESTful API service built with Django REST Framework (DRF) that integrates Meta's LLM, Llama 3, to analyze the contents of a GitHub pull request (PR). The application leverages Celery for asynchronous task management and Redis as a database backend.

## Features

- Extracts PR details from a given GitHub repository.
- Sends PR content to Llama 3 LLM for analysis via the Groq API.
- Supports both public and private repositories.
- Provides two API endpoints for task initiation and status checking.

## Technology Stack

- **Backend Framework**: Django REST Framework (DRF)
- **Task Management**: Celery
- **Database Backend**: Redis
- **LLM Integration**: Meta's Llama 3 (via Groq API)
- **External APIs**: GitHub API, Groq API

## API Endpoints

To start a task:
```
/api/start_task/
```
Send :
```json
{
    "github_url": "https://github.com/django/django",
    "pr_number": 19044
}


```
### Note regarding github tokens:

To access your own private repos or if 'there was an error with your request.' error occurs when checking the status of the task , Then you must provide your own github private token.
To generate your Github personal access token -

Visit the https://github.com/settings/personal-access-tokens section on Github.
- Click on Generate new token
- Fill in the token name, expiry and resource owner
- Carefully review and grant the necessary fine grained permissions to your token
- Use the generated token here
```json
{
    "github_url": "https://github.com/django/django",
    "pr_number": 19020,
    "github_token":"<your token here>"
}

```

To check the status of the task:
```
/api/check_task/<task_id>
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ismailrazak/Github-Pull-Request-Reviewer-API.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```
## Set Up Environment Variables

Create a `.env` file in the project root and configure the following variables:

```
GROQ_API_KEY=<your_groq_api_key>
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```
## Run Redis Server
Ensure Redis is running on your system. If not installed, refer to the [Redis installation guide](https://redis.io/download).

## Start Celery Worker
Run the following command to start the Celery worker:

```bash
celery -A main worker - l info -P eventlet
```