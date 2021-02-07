from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}' # f'{출력할 원하는 변수를 넣을 수 있다}'
