from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Major(models.Model):
    name=models.CharField(max_length=255, default='no name')
    image = models.ImageField(default='../media/lect.jpg' ,blank=True)
    def __str__(self):
        return self.name


class setting(models.Model):
    WelcomePageText = models.CharField(max_length=255,blank=True, null=True)


class Subject(models.Model):
    name=models.CharField(max_length=255, default='no name')
    major=models.ForeignKey(Major ,  on_delete=models.CASCADE ,null=True,blank=True , related_name="item")
    def __str__(self):
        return self.name

class Section(models.Model):
    name=models.CharField(max_length=255, null=True,blank=True)
    subject=models.ManyToManyField(Subject ,null=True,blank=True , related_name="section" )
    isPublic=models.BooleanField(default=True,blank=True,null=True)
    def __str__(self):
        return self.name

class email(models.Model):
    email=models.EmailField(max_length=255, null=True,blank=True)
    canAccess=models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return self.email


class Media(models.Model):
    name=models.CharField(max_length=255, default='no name')
    link=models.URLField(null=True , blank=True)
    file=models.FileField(upload_to='videos_uploaded',null=True , blank=True)
    video=models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], blank=True)
    image=models.ImageField(null=True , blank=True)
    Subject=models.ForeignKey(Subject , on_delete=models.CASCADE ,null=True,blank=True , related_name="item")
    section=models.ForeignKey(Section , on_delete=models.CASCADE , default='' ,related_name='media')
    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name=models.CharField(max_length=255)
    number=models.IntegerField(null=True,blank=True)


