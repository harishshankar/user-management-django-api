from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserManagementList.as_view()),
    path('users/<int:pkey>/', UserManagementDetail.as_view()),
    # path('auth/', LoginView.as_view()),
]
