from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, advisor_serializer, booking_serializer, full_details_booking
from django.contrib.auth.models import User
from .models import advisor, booking
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
#Register API

class addadvisor(APIView):

    def post(self, request):
        seriailzer = advisor_serializer(data = request.data)

        if seriailzer.is_valid():
            seriailzer.save()
            return Response(status = status.HTTP_201_CREATED )
        return Response(seriailzer.errors, status = status.HTTP_400_BAD_REQUEST )

class get_advisors(APIView):
    def get(self, request, pk):
        advisors_list = advisor.objects.all()
        serializer = advisor_serializer(advisors_list, many= True)
        return Response(serializer.data, status = status.HTTP_200_OK )


class add_booking(APIView):
    def post(self, request, pk, id):
        advisor_ = advisor.objects.get(pk = id)
        serializer = booking_serializer(data = request.data)
        if serializer.is_valid():
            new_booking = booking.objects.create(advisor_name = advisor_.advisor_name, photo_url = advisor_.photo_url, advisor_id = advisor_.id, booking_time = serializer.data['booking_time'], user = pk)
            print("Created")
        else:
            print("Not created")
        return Response(status = status.HTTP_200_OK )

class get_booking(APIView):
    def get(self, request, id):
        advisors = booking.objects.all().filter(user = id)
        serializer = full_details_booking(advisors, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)




