from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('pet/add/', views.add_pet, name='pet_create'),   # Add pet
    path('pet/<int:pk>/edit/', views.edit_pet, name='pet_edit'),  # Edit pet
    path('pet/<int:pk>/delete/', views.delete_pet, name='pet_delete'),  # Delete pet
    path('signup/', views.signup_view, name='signup'),
    path('', views.pet_list, name='pet_list'),
]
