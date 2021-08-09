from django.urls import path

from commentapp.views import CommentCreateView

app_name = 'commentapp'  #commentapp:

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),


]