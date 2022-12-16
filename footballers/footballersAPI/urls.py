from django.urls import path, include
from footballersAPI import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'footballers', views.FootballerViewSet, basename='footballers')

urlpatterns = [
    # path('v1/footballers/', views.FootballerAPIList.as_view()),
    # path('v1/footballers/<int:pk>/', views.FootballerAPUpdate.as_view()),
    # path('v1/footballerdetail/<int:pk>/', views.FootballerDetailAPIView.as_view()),
    
    # path('v1/footballers/', views.FootballerViewSet.as_view({'get': 'list'})),
    # path('v1/footballers/<int:pk>/', views.FootballerViewSet.as_view({'put': 'update'})),
    
    
    # http://127.0.0.1:8000/api/v1/footballers/
    # http://127.0.0.1:8000/api/v1/footballers/1/
    path('v1/', include(router.urls)),  
]