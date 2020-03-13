from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, related_name="coordinatorName", on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        template = '{0.websiteName} {0.Uploader_info}'
        return template.format(self)
