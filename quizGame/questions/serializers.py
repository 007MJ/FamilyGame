from rest_framework import serializers
from questions.models import BooleanQestion, MultichoiceQuestion

class BooleanQestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooleanQestion
        fields = ['id', 'question', 'answer_one', 'answer_two', 'correct_answers']


class MultichoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultichoiceQuestion
        fields = ['id', 'question',  'multiChoice', 'correct_answers']
        