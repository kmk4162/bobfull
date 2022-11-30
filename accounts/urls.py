from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import urls
from .views import GetCSRFToken

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('csrf_cookie/', GetCSRFToken.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)