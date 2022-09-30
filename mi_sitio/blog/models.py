from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PostTwo(models.Model):
    col1 = models.IntegerField(blank=True, null=True)
    col2 = models.CharField(max_length=1,blank=True, null=True)
    col3 = models.IntegerField(blank=True, null=True)
    col4 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.col1)+ (' , ') + str(self.col2)+ (' , ') + str(self.col3) + (' , ') + str(self.col4)