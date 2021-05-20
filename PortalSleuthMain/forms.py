from django import forms
from .models import ReviewModel,EmojiReviewModel
from crispy_forms.helper import FormHelper

class ReviewForm(forms.ModelForm):
    class Meta:
        model=ReviewModel
        fields=['review']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class EmojiReviewForm(forms.ModelForm):
    class Meta:
        model=EmojiReviewModel
        fields=['emotion']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
