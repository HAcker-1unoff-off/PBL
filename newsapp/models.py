from email.policy import default
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    source = models.CharField(max_length=255)
    category = models.CharField(max_length=50, default="general")
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

class Poll(models.Model):
    question = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text