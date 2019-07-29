from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    # 이미지를 DB에 넣고 싶을 때 pillow 모듈 설치!