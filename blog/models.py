from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #文字制限
    title = models.CharField(max_length=200)
    #文字無制限
    text = models.TextField()
    #日付と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    #他のモデルへのリンク
    published_date = models.DateTimeField(blank=True, null=True)

#公開用のメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
