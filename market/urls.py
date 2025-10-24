from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('pet/add/', views.add_pet, name='pet_create'),
    path('pet/<int:pk>/edit/', views.edit_pet, name='pet_edit'),
    path('pet/<int:pk>/delete/', views.delete_pet, name='pet_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.pet_list, name='pet_list'),
    path('logout/', views.logout_view, name='logout'),

    # Logout view (works with POST form)
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
