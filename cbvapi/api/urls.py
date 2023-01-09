from django.urls import path

from cbvapi.api import views

urlpatterns=[ 
    path('mcbvlist/',views.MovieListAV.as_view(),name='mcbvlist'),
    path('mcbvone/<int:pk>/',views.MovieDetailAV.as_view(),name='mcbvone'),
]