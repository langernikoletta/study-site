from django.contrib import admin
from .models import Lesson

# дозволяє керувати уроками через адмінку
admin.site.register(Lesson)