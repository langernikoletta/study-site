from django.db import models
from django.contrib.auth.models import User
import urllib.parse as urlparse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Панель з всіма класами
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
    
    #Функ, яка витягує ID з твого поля video_url
    def get_youtube_id(self):
        if not self.video_url:
            return None
        
        url_data = urlparse.urlparse(self.video_url)
        query = urlparse.parse_qs(url_data.query)
        
        if 'v' in query:
            return query['v'][0]
        
        path = url_data.path.split('/')
        if path:
            return path[-1]
        return None

    def __str__(self):
        return f"{self.title} - {self.school_class} клас - {self.content[:100]}..."


class UserLessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Користувач")
    # Поле для аватара (буде зберігатися в папку avatars/)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True, null=True, verbose_name="Аватар")
    # Поле для інформації про себе
    bio = models.TextField(max_length=500, blank=True, verbose_name="Про себе")

    def __str__(self):
        return f"Профіль користувача {self.user.username}"

# Автоматично створюємо профіль, коли створюється новий користувач
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)