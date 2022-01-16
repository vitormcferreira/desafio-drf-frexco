from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views


router = DefaultRouter()
router.register('region', views.RegionViewSet)
router.register('fruit', views.FruitViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Documentação
    path('schema/', SpectacularAPIView().as_view(), name='schema'),
    # link para a visualização da API
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
