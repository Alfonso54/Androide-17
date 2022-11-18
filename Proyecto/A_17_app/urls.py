from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name="index"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('subirauto/', views.subirauto, name="subirauto"),
    path('verautos/', views.verautos, name="verautos"),
    path('revisarautos/<int:pk>', views.revisarautos, name="revisarautos"),
    path('borrarauto/<int:pk>', views.borrarauto, name="borrarauto"),
]