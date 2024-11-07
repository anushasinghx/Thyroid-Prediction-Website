# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('thyroid_test_results/', views.thyroid_test_results, name='thyroid_test_results'),
     path('test/', views.test_view, name='test'),  # Prediction endpoint
]
