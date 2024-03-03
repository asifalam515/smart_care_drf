from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter() #amader router

router.register('', views.ContactusViewSet) #router er route create kore fellam
urlpatterns = [
    path('', include(router.urls)),
]
