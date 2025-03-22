from django.db import models

# Create your models here


class Integration(models.Model):
    name = models.CharField(max_length=255)
    api_url = models.URLField(unique=True)
    slack_channel = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    jira_project = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class APISpec(models.Model):
    integration = models.ForeignKey(Integration, on_delete=models.CASCADE)
    fetched_at = models.DateTimeField(auto_now_add=True)
    spec_data = models.JSONField()

    def __str__(self):
        return f"{self.integration.name} - {self.fetched_at}"
