from django.db import models

# Create your models here.
# 각 모델은 :class:`django.db.models.Model`의 하위 클래스로 표현된다
# 모델마다 여러 클래스 변수가 있으며 각 클래스 변수는 모델에서 데이터베이스 필드를 나타낸다


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

