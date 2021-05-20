from django.contrib import admin
from .models import CategoryModel,ReviewModel,EmojiReviewModel
# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ReviewModel)
admin.site.register(EmojiReviewModel)
