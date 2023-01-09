from django.urls import path

from restapp.api import views

urlpatterns=[ 
    path('mlist/',views.movielist,name='mlist'),
    path('mone/<int:pk>/',views.movieone,name='mone'),
]