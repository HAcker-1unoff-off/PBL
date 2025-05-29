from django.db import models

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