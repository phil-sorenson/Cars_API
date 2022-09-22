from django.urls import path
from . import views  # WHY JUST 'from ." ??

urlpatterns = [
    path('', views.cars_list),
]