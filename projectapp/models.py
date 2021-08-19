from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description =models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # 어떤 문자로 되돌려준 것 인지
        return self.name