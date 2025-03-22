import requests
import json
from celery import shared_task
from jsondiff import diff
from .models import Integration, ApiSpec
from celery.schedules import crontab

app.conf.beat_schedule = {
    "check-api-every-hour": {
        "task": "monitor.tasks.check_api_changes",
        "schedule": crontab(minute=0, hour="*"),  # Runs every hour
    },
}


@shared_task
def check_api_changes():
    integrations = Integration.objects.all()

    for integration in integrations:
        response = requests.get(integration.api_url)
        if response.status_code == 200:
            new_spec = response.json()

            # Get last stored API spec
            last_spec = ApiSpec.objects.filter(
                integration=integration).order_by('-fetched_at').first()
            if last_spec:
                changes = diff(last_spec.spec_data, new_spec)

                if changes:
                    alert_changes(integration, changes)

            # Save the new spec
            ApiSpec.objects.create(integration=integration, spec_data=new_spec)


def alert_changes(integration, changes):
    message = f"Breaking changes detected in {integration.name}:\n{json.dumps(changes, indent=2)}"

    # Send Slack alert
    if integration.slack_channel:
        send_slack_alert(integration.slack_channel, message)

    # Send Email alert
    if integration.email:
        send_email_alert(integration.email, "API Change Alert", message)

    # Create Jira ticket
    if integration.jira_project:
        create_jira_ticket(integration.jira_project,
                           f"Breaking Change in {integration.name}", message)


def send_slack_alert(channel, message):
    from slack_sdk import WebClient
    client = WebClient(token="xoxb-your-slack-token")
    client.chat_postMessage(channel=channel, text=message)


def send_email_alert(to_email, subject, body):
    from smtplib import SMTP
    from email.message import EmailMessage

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "your-email@example.com"
    msg["To"] = to_email

    with SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your-email@example.com", "your-email-password")
        server.send_message(msg)


def create_jira_ticket(project, summary, description):
    from jira import JIRA
    jira = JIRA(server="https://your-jira-instance.atlassian.net",
                basic_auth=("your-jira-email@example.com", "your-jira-api-token"))
    jira.create_issue(project=project, summary=summary,
                      description=description, issuetype={"name": "Bug"})
