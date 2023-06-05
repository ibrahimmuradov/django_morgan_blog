from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:id>/', views.post, name='post'),
    path('delete-comment/', views.delete_comment, name='delete-comment'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
]