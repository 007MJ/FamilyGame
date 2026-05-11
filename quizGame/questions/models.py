from django.db import models

# Create your models here.

class BooleanQestion(models.Model):
    question = models.CharField(max_length=100)

    answer_one = models.CharField(max_length=100)
    answer_two = models.CharField(max_length=100)

    correct_answer = models.CharField(max_length=100) 





class AnswerChoice(models.Model):
     answer = models.CharField(max_length=100)


class MultichoiceQuestion(models.Model):
      question = models.CharField(max_length=100)
      multiChoice = models.ForeignKey(AnswerChoice, on_delete=models.CASCADE , related_name='MultichoiceQuestion')
      correct_answers = models.ForeignKey(AnswerChoice, on_delete=models.CASCADE)

