from rest_framework import serializers
from . import models

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Media
        fields=[ "name","link","file","video", "image" ,'section']



class SectionSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.Section
        fields = ['id','name','subject','isPublic']
class EmailsSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.email
        fields = ['id','email','canAccess']


class SubjectSerializer(serializers.ModelSerializer):
     item = MediaSerializer(many=True,read_only=True)
     section = SectionSerializer(many=True,read_only=True)
     class Meta:
        model = models.Subject
        fields = ['name','id','item','major','section']

class MajorSerializer(serializers.ModelSerializer):
     item = SubjectSerializer(many=True,read_only=True)
     class Meta:
        model = models.Major
        fields = ['name','id','item']

class SimpleMajorSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.Major
        fields = ['name','id','image']

class settingsSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.setting
        fields = ['WelcomePageText','id']

class DoctorsSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.Doctor
        fields = ['id','name','number']


