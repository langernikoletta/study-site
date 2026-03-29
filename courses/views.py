from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Lesson

# Твоя функція для списку курсів (залишається як була)
def course_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'courses/course_list.html', {'lessons': lessons})

# НОВА функція для реєстрації користувачів
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматичний вхід після реєстрації
            return redirect('course_list') # Повертаємо на головну
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})