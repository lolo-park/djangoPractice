import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# 각 모델은 :class:`django.db.models.Model`의 하위 클래스로 표현된다
# 모델마다 여러 클래스 변수가 있으며 각 클래스 변수는 모델에서 데이터베이스 필드를 나타낸다


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

