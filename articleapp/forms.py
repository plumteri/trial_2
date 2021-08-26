from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'min-height: 10red;'
                                                                    'text-align: left;'}))  # 문자열 입력받는 textarea라는 위젯사용 클래스를 에디터블로 가지는

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']