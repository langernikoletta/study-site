from django.shortcuts import render
from .models import Lesson
def register(request):

    return render(request, 'registration/register.html')
def course_list(request):

    class_filter = request.GET.get('class_num') 
    
    if class_filter:
        lessons = Lesson.objects.filter(school_class=class_filter)
    else:
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
            login(request, user)
            return redirect('course_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Lesson



def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})


from django.core.paginator import Paginator
def course_list(request):
    lesson_list = Lesson.objects.all().order_by('-id')
    paginator = Paginator(lesson_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'courses/course_list.html', {'page_obj': page_obj})


from django.contrib.auth.decorators import login_required

@login_required # Тепер сюди пустить тільки після введення логіну/паролю щоб аноніми не заходили
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})




from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Твій профіль успішно оновлено!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'courses/profile.html', context)