from django.shortcuts import render
from .models import Lesson
def register(request):
    # Тут буде логіка реєстрації користувача
    return render(request, 'registration/register.html')
def course_list(request):
    # Дивимось, чи передав користувач клас в посиланні
    class_filter = request.GET.get('class_num') 
    
    if class_filter:
        # Якщо клас вибрано, фільтруємо базу
        lessons = Lesson.objects.filter(school_class=class_filter)
    else:
        # Якщо нічого не вибрано, аабсолютно показуємо всі уроки
        lessons = Lesson.objects.all()
    
    return render(request, 'courses/course_list.html', {'lessons': lessons})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматично логінимо після реєстрації
            return redirect('course_list') # Повертаємо до головної
    else:
        form = UserCreationForm()
    
    # Вказуємо шлях до твого гарного шаблону
    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Lesson

# ... твої інші функції (course_list, register) ...

def lesson_detail(request, lesson_id):
    # Шукаємо урок за ID, якщо не знайдемо — видасть помилку 404
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})