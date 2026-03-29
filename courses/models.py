from django.db import models

# Create your models here.
#панель з класами
class Lesson(models.Model):
    CLASS_CHOICES = [
        ('7', '7 Клас'),
        ('8', '8 Клас'),
        ('9', '9 Клас'),
        ('10', '10 Клас'),
        ('11', '11 Клас'),
    ]
    title = models.CharField(max_length=200, verbose_name="Назва теми")
    school_class = models.CharField(max_length=2, choices=CLASS_CHOICES, verbose_name="Клас")
    content = models.TextField(verbose_name="Зміст теми")
    video_url = models.URLField(blank=True, null=True, verbose_name="Посилання на відео")
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True, verbose_name="PDF файл")
    def __str__(self):
        return f"{self.title} - {self.school_class} клас - {self.content[:100]}..."