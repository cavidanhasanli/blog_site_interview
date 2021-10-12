from django import forms
from base_app.models import PostContactModel, PostModel
from ckeditor.widgets import CKEditorWidget


class PostContactForm(forms.ModelForm):
    class Meta:
        model = PostContactModel
        fields = '__all__'


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['post_title', 'post_subtitle', 'post_text','post_head_image']