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