from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Result)

class QuestionInline(admin.TabularInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

