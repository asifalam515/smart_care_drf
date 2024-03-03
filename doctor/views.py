from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor,Designation,AvailableTime,Specialization,Review
from .serializers import DoctorSerializer,DesignationSerializer,AvailableTimeSerializer,SpecializationSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission,SAFE_METHODS,IsAuthenticatedOrReadOnly

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    
class SpecializationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer