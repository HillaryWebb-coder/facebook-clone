from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardView, name="dashboard"),
    path('register/', views.registerView, name="register"),
    path("edit/", views.editProfileView, name="edit_profile"),
]
