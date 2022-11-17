from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('<int:post_id>/', views.post_detail, name='post_detail')
]
