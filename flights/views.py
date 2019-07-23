from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializers , BookingSerializer




class FlightList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializers 

class BookingList(ListAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

