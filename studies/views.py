from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet ,ModelViewSet
from .serializer import SubjectSerializer ,MajorSerializer ,SimpleMajorSerializer,DoctorsSerializer ,SectionSerializer ,EmailsSerializer
from rest_framework.permissions import IsAdminUser,AllowAny
# Create your views here.
from .models import Subject ,Major ,Doctor,Section,email
class SubjectViewSet(ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class MajorViewSet(ReadOnlyModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class SimpleMajorViewSet(ReadOnlyModelViewSet):
    queryset = Major.objects.all()
    serializer_class = SimpleMajorSerializer

class DoctorsViewSet(ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer

class SectionViewSet(ReadOnlyModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class EmailViewSet(ModelViewSet):
    queryset = email.objects.all()
    serializer_class = EmailsSerializer
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method =='POST':
            return [AllowAny()]
        else:
            return [IsAdminUser()]


class MajorSubjectViewSet(ReadOnlyModelViewSet):
    serializer_class = SubjectSerializer
    def get_queryset(self):
        
        if self.kwargs['major_pk']:
            return Subject.objects.filter(major=self.kwargs['major_pk'])
        else:
            return Subject.objects.all()