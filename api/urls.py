from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('region', views.RegionViewSet)
router.register('fruit', views.FruitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
