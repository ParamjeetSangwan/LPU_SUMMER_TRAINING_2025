from django.urls import path

from marketplace import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
]