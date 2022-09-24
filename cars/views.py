from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car
from rest_framework import status
# # Where we will define all of the functions that the outside world can interact with through URLs over internet
# Create your views here.

# Create a function to define what request types that ifunction is capable of handling (every api_view func. should take in a request)
@api_view(['GET','POST'])

def cars_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data) 
    
    elif request.method == 'POST':
        serializer = CarSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)  # <--- Code to validate the request coming in via Postman or frontend
        serializer.save()   
    return Response(serializer.data, status=status.HTTP_201_CREATED) 

        
