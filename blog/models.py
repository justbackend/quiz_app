from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

dif_choices = (
    ("e", "easy"),
    ("m", "medium"),
    ("h", "hard")
)

class Quiz(models.Model):
    name = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    number_of_questions = models.PositiveIntegerField()
    time = models.PositiveIntegerField(help_text="duration of the quiz")
    required_score_to_pas = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=1 , choices=dif_choices)

    def __str__(self):
         return f"{self.name}: {self.topic}"

    def get_questions(self):
        return self.question.all()
class Question(models.Model):
    text = models.CharField(max_length=500)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answers.all()

class Answer(models.Model):
    text = models.CharField(max_length=150)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    time = models.DateTimeField(auto_now_add=True, null= True, blank= True)

    def __str__(self):
        return f"{self.user.username}: {str(self.score)}"


