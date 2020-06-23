from django.db import models

# Create your models here.

class Study(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)
    category = models.IntegerField(default=0) # 1: dev, 2: univ, 3: others
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    # image = models.ForeignKey(Photo, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Paragraph(models.Model):
    number = models.IntegerField(default=-1) # study에서의 순서 
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now=True)

    study = models.ForeignKey(Study, on_delete=models.CASCADE)

    def __str__(self):
        return '#{}의 #{} 번째 단락'.format(self.study, self.number)

