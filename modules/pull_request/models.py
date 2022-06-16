from django.db import models


# Pull Requests Model
class PullRequest(models.Model):
    """
        PullRequest Model
    """
    
    class StatusChoices(models.TextChoices):
        OPEN = 'open', 'open'
        MERGED = 'merged', 'merged'
    
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=6, choices=StatusChoices.choices, default=StatusChoices.OPEN)
    number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
