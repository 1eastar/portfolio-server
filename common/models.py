from django.db import models

# Create your models here.

class Contact(models.Model):
    writer = models.CharField(max_length=10)
    title = models.CharField(max_length=25)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return '{}에서 온 contact : {}'.format(self.writer, self.title)