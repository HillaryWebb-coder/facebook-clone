from django.urls import path

# Custom Imports
from . import views

app_name = "images"

urlpatterns = [
    path('', views.imageListView, name="image_list"),
    path('new-image/', views.newImageView, name="create_image"),
    path('like-image/', views.likeImageview, name="like_image"),
]
