from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car
# # Where we will define all of the functions that the outside world can interact with through URLs over internet
# Create your views here.

# Create a function to define what request types that ifunction is capable of handling (every api_view func. should take in a request)
@api_view(['GET'])
def cars_list(resuest):
    cars = Car.objects.all()
 
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data) 

# First response after running server:
    # Page not found (404)
    # Request Method:	GET
    # Request URL:	http://127.0.0.1:8000/cars
    # Using the URLconf defined in car_project.urls, Django tried these URL patterns, in this order:

    # admin/
    # The current path, cars, didn’t match any of these.

    # You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.

        # REASON FOR THIS ---> cars app and car_project both have urls.py files TO FIX ---> Register our cars urls.py file with our project urls.py file
            # 
