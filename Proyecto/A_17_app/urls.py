from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('subirauto/', views.subirauto, name="subirauto"),
    path('verautos/', views.verautos, name="verautos"),
    path('revisarautos/<int:pk>', views.revisarautos, name="revisarautos"),
    path('borrarauto/<int:pk>', views.borrarauto, name="borrarauto"),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',views.NewRegister,name="register"),
    path('logout/',LogoutView.as_view(),name="logout"),
]