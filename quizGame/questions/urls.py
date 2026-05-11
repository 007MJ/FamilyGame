from django.urls import path
from questions.views import *

urlpatterns = [
    path('booleanquestion/', BooleanQuestion.as_view()),
]