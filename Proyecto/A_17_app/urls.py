from django.urls import include, path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('subirauto/', views.subirauto, name="subirauto"),
    path('verautos/', views.verautos, name="verautos"),
    path('revisarautos/<int:pk>', views.revisarautos, name="revisarautos"),
]