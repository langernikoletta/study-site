from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка зі списком уроків
    path('', views.course_list, name='course_list'),
    
    # Реєстрація (твій кастомний view)
    path('register/', views.register, name='register'),
    
    # Особистий кабінет (Профіль)
    path('profile/', views.profile_view, name='profile'),
    
    # Сторінка окремого уроку
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
]