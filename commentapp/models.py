from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,  #연결되어있는 삭제됐을 때 지우진 않고 연결된 게시글이 널이채로 둔다
                                related_name='comment', null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)

    content = models.TextField(null=False)  # 장문

    created_at =models.DateTimeField(auto_now_add=True) #날짜와 시간