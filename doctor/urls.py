from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AvailableTimeViewSet,DoctorViewSet,SpecializationViewSet,ReviewViewSet,DesignationViewSet

router = DefaultRouter()
router.register('list',DoctorViewSet)
router.register('specialization',SpecializationViewSet)
router.register('available_time',AvailableTimeViewSet)
router.register('designation',DesignationViewSet)
router.register('review',ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]