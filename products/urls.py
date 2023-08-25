from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreate.as_view()),
    path('<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view()),
    path('product/<int:pk>/delete/', views.ProductDestroy.as_view()),
    path('characteristics/', views.CharacteristicListCreate.as_view()),
    path('characteristics/<int:pk>/', views.CharacteristicRetrieveUpdateDestroy.as_view()),
    path('characteristics/<int:pk>/delete/', views.CharacteristicDestroy.as_view()),
]