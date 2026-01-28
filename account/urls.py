from rest_framework import routers
from django.urls import path, include
from account import views
from account.views import LoginApi, RegisterApi

router = routers.DefaultRouter()
router.register('account', views.UserViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginApi.as_view()),
    path('register/', RegisterApi.as_view()),
]
