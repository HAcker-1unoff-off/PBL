from django.contrib import admin
from .models import Article, Poll, Choice

admin.site.register(Article)
admin.site.register(Poll)
admin.site.register(Choice)

# Register your models here.
