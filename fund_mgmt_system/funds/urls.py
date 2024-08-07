from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FundViewSet, TestAPIView

router = DefaultRouter()
router.register(r'funds', FundViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/test/', TestAPIView.as_view(), name='test_api'),
    # path('api/funds/', FundViewSet.as_view(), name='fund_list')
]
