from django.urls import path,include
from .views import RegisterView,StudentView



urlpatterns = [
    path('register/',RegisterView.as_view(),name='regiser'),
    path('student/',StudentView.as_view(),name='student'),
    path('auth/',include('rest_framework.urls')),
]
