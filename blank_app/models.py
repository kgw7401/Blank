from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.
class NewBlank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    blank_on_off = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class BlankContent(models.Model):
    refer = models.TextField()
    memo = models.TextField()
    new_blank = models.ForeignKey('NewBlank', on_delete=models.CASCADE, related_name='blankcontent')

    # 만약 ForeignKey의 필드를 사용하고 싶다면 ForeignKey의 변수를 사용
    def __str__(self):
        return '[{}] {}'.format(self.new_blank.title, self.refer)
