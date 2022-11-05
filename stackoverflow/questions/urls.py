from django.urls import path

from . import views

urlpatterns = [
    path('working', views.forecast_view, name='view1'),
    path('notworking', views.forecast_view2, name='view2'),
]