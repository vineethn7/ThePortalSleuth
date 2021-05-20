from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class CategoryModel(models.Model):
    categoryName=models.CharField(max_length=255)
    websiteName=models.CharField(max_length=255)
    url=models.CharField(max_length=300)

    def __str__(self):
        return self.websiteName

class ReviewModel(models.Model):
    Uploader_info = models.CharField(max_length=100, editable=False, null = True)
    websiteName = models.CharField(max_length=100,blank=False)
    review = models.TextField(max_length=1000,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        template = '{0.websiteName} {0.user.username}'
        return template.format(self)
    def get_absolute_url(self):
        return reverse('submit-review', kwargs={'pk': self.pk})

class EmojiReviewModel(models.Model):
    Uploader_info = models.CharField(max_length=100, editable=False, null = True)
    websiteName = models.CharField(max_length=100,blank=False)
    emotion=models.CharField(max_length=100,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        template = '{0.websiteName} {0.user.username} {0.emotion}'
        return template.format(self)
    # def get_absolute_url(self):
    #     return reverse('submit-emoji', kwargs={'pk': self.pk})
