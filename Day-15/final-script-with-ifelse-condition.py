### DevOps Task: Automate Jira Ticket Creation Based on GitHub Issue Comments using Flask Webhook

## Titles:
## GitHub Issue Comment to Jira Automation Script
## Automated Jira Ticket Creation from GitHub Issue Comments
## Webhook-based Integration for GitHub to Jira Ticketing
## DevOps Workflow: GitHub → Jira Ticket Auto-Creation
## Flask Webhook for Auto-Creating Jira Tickets from GitHub

import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    # Extract comment body from GitHub issue_comment payload
    body = request.json.get("comment", {}).get("body", "").strip()

    # Only proceed if the comment is exactly "/jira"
    if body == "/jira":
        url = "https://acldigital-team-a8o8ioi3.atlassian.net/rest/api/3/issue"
        API_TOKEN = "ATATT3xFfGF0dSRm05r6PbbAUSmYEQcs-gkPblMNS3JCwdd4jokeZEsnkdmhyyn4mKZP4UmLB74Bq0cU_f7BLS5aRb6sIQp1lkUdPx6D7_9nfcbuJQHWYDP5IWB79J03sbjXnBrr-YN6BCI6RVk2JZd84mT4jANbyiDbQ7dceDxtVnXQVIqsS3c=125242F3"
        auth = HTTPBasicAuth("nashit.baig@acldigital.com", API_TOKEN)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Order entry fails when selecting supplier.",
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                },
                "project": {
                    "key": "SCRUM"
                },
                "issuetype": {
                    "id": "10004"
                },
                "summary": "Main order flow broken"
            },
            "update": {}
        })

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        # Only respond to exact "/jira" comments
        return "only /jira is allowed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

### Output:
ubuntu@ip-172-31-90-27:/mnt/python_scripts$ sudo python3 final-one.py 
 * Serving Flask app 'final-one'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.31.90.27:5000
Press CTRL+C to quit

### Note added if else condition in above code:
In this add one if condition if body == /jira only then perform the api creation
add this condition in this block requests.request populate entire into a if block and else condition comment should be /jira only.

