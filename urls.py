from django.urls import path, include
from rest_framework import routers
from account.views import UserViewSet
from .view import SocialLoginView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('oauth/', SocialLoginView.as_view()),

]