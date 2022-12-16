from django.urls import path
from footballersAPI import views

urlpatterns = [
    path('v1/footballers/', views.FootballerAPIList.as_view()),
    path('v1/footballers/<int:pk>/', views.FootballerAPUpdate.as_view()),
    path('v1/footballerdetail/<int:pk>/', views.FootballerDetailAPIView.as_view()),
]