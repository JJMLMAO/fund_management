from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FundViewSet

router = DefaultRouter()
router.register(r'funds', FundViewSet)

urlpatterns = [
    path('', include(router.urls))
]
