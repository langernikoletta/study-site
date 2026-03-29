from django.shortcuts import render
from .models import Lesson

def course_list(request):
    # Отримуємо всі уроки з моєї бази даних
    lessons = Lesson.objects.all()
    # Передаємо їх у HTML-файл для відображення
    return render(request, 'courses/course_list.html', {'lessons': lessons})