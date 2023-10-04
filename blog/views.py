from django.shortcuts import render, redirect
from .models import *
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.

def index(request, pk):
    now = datetime.now()
    end_time = now + timedelta(minutes=Quiz.objects.get(id=pk).time)
    content = {
        "quiz": Quiz.objects.get(id=pk),
        "questions": Question.objects.filter(quiz_id=pk),
        "answers": Answer.objects.filter(question__quiz_id=pk),
        "now": now,
        "end_time": end_time,
    }
    now = datetime.now()
    end_time = now+timedelta(minutes=Quiz.objects.get(id=pk).time)

    if request.method == "POST":
        quiz = Quiz.objects.filter(id=pk)
        questions = Question.objects.filter(quiz_id=pk)
        score = 0

        for question in questions:
            selected_option = request.POST.get(f"question_{question.id}")
            if selected_option is not None:
                given_answer = Answer.objects.get(id=selected_option).text
                right = question.answers.get(correct=True)
                if given_answer == right.text:
                    score+=1

        Result.objects.create(quiz=Quiz.objects.get(id=pk), user=request.user, score=score)
        return redirect("/score/")
    return render(request, 'index.html', content)

def home(request):
    content = {
        'quizes': Quiz.objects.all()
    }
    return render(request, 'home.html', content)

def score(request):
    content = {
        "results": Result.objects.all()
    }
    return render(request, 'score.html', content)

def create_quiz(request):
    if request.method == "POST":
        js_variable = int(request.POST.get('js_variable', None))

        # quiz = Quiz.objects.create(
        #     name = request.POST['quizName'],
        #     topic = request.POST['topic'],
        #     number_of_questions= js_variable,
        #     time = request.POST['duration'],
        #     required_score_to_pas = request.POST['passScore'],
        #     difficulty = request.POST['difficulty']
        # )
        # quiz.save()
        # quiz_id = quiz.id

        for i in range(1, js_variable+1):
            question_name = f"question{i}"
            question = request.POST[question_name]
            print(question)

        # Question.objects.create()
    return render(request, 'create_quiz.html')
