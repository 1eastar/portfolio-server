from django.db import models

from colorfield.fields import ColorField

# Create your models here.

class Experience(models.Model):
    main_title = models.CharField(max_length=50)
    main_image = models.ImageField(upload_to="image", null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    temporary = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    # main_title_color = models.CharField(max_length=10, default='')
    main_title_color = ColorField(default='#303030')

    def __str__(self):
        return self.main_title


class PhotoText(models.Model):
    number = models.IntegerField(default=-1)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    no_underline = models.BooleanField(default=False)
    vertical_mode = models.BooleanField(default=False)

    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return 'experience #{}의 photo with text #{}'.format(self.experience, self.number)