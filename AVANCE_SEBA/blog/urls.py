from django.urls import include, path
from blog import views

urlpatterns = [
    path('homepageindex/',views.homepagecolor,name='homepageindex'),
]