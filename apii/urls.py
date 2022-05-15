from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.movieList.as_view()),
    path('<int:pk>/',views.movieDetail.as_view())
]