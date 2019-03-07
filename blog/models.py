from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # image = models.ImageField(default='default.png', blank=True)
    image = models.FileField(default='default.png', blank=True)
    # uploaded_at = models.DateTimeField(auto_now_add=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# class UploadFileModel(models.Model):
#     title = models.TextField(default='')
#     file = models.FileField(null=True)
