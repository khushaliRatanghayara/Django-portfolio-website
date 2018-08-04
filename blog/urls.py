from django.urls import path,include
from .views import bloglist,blog_details

urlpatterns = [
    path('blog/',bloglist),
    path('<int:blog_id>/',blog_details,name = "detail"),
    path('',bloglist),
]