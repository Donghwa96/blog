from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title   # admin화면에서 타이틀 값이 나옴.

    def summary(self):
        return self.body[:100]