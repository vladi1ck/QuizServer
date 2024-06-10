from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.models import Place, Trip
from core.serializers import AuthUserLoginSerializer, AuthUserRegistrationSerializer, PlaceSerializer, TripSerializer


# Create your views here.
class AuthUserLoginView(GenericAPIView):
    serializer_class = AuthUserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'authenticatedUser': {
                    'username': serializer.data['username'],
                    'id': serializer.data['id'],
                }
            }

            return Response(response, status=status_code)


class AuthUserRegistrationView(GenericAPIView):
    serializer_class = AuthUserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data["username"]
            }

            return Response(response, status=status_code)


class PlaceView(GenericAPIView):
    serializer_class = PlaceSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        places = Place.objects.all()
        print(places)
        serializer1 = PlaceSerializer(places, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched values',
            'places': serializer1.data,
        }
        return JsonResponse(response, status=status.HTTP_200_OK)


class TripView(GenericAPIView):
    serializer_class = TripSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        trips = Trip.objects.all()
        serializer1 = self.serializer_class(trips, many=True)

        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched values',
            'trips': serializer1.data,

        }
        return JsonResponse(response, status=status.HTTP_200_OK)
