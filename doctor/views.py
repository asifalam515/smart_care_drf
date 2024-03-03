from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor,Designation,AvailableTime,Specialization,Review
from .serializers import DoctorSerializer,DesignationSerializer,AvailableTimeSerializer,SpecializationSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission,SAFE_METHODS,IsAuthenticatedOrReadOnly
from rest_framework import filters,pagination


# Create your views here.


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 #items per page
    page_size_query_param = page_size
    max_page_size =100
    
class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    
    
class SpecializationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
from rest_framework import filters

class AvailableTimeforSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

            
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeforSpecificDoctor]
    
    

    
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer