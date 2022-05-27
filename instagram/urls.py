from . import views
from django.urls import path
app_name = 'instagram'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/edit/', views.post_detail, name='post_edit'),
    path('<int>:pk/delete/', views.post_list, name='post_delete'),
    path('<int:pk>', views.post_detail, name='post_detail'),


]