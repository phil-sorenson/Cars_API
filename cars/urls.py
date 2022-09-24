from django.urls import path
from . import views  # WHY JUST 'from ." ??

urlpatterns = [
    path('', views.cars_list),
    path('<int:pk>/', views.car_detail),    # < > are VERY important--allows item to be passed

]

# 