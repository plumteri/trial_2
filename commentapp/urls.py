from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

app_name = 'commentapp'  #'commentapp:detail'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),

]