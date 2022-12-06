from django.urls import include, path
from . import views 
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import admin

urlpatterns = [
    path('inicio/',views.inicio,name="inicio"),
    path('pub1/',views.pub1,name="pub1"),
    path('pub2/',views.pub2,name="pub2"),
    path('pub3/',views.pub3,name="pub3"),
    path('admin/', admin.site.urls),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('like/<int:pk>', views.darlike, name='dar_like'),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout"),]