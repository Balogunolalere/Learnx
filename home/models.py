from django.db import models
from django_quill.fields import QuillField


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(blank=True,null=True)
    body = QuillField()
    upload_lecture = models.FileField(blank=True,null=True,upload_to='uploads/')

    def __str__(self):
        return self.name

class Question(models.Model):
    statement = models.CharField(max_length=200)
    self_check = models.BooleanField(default=False)
    predefined_answer = models.CharField(max_length=200,blank=True,null=True)
    predefined_remark = models.CharField(max_length=200,blank=True,null=True)
    course_id = models.IntegerField(default=0)

    def __str__(self):
        return self.statement


