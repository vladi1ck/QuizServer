from django.urls import path

from core import views
from core.views import AuthUserRegistrationView, AuthUserLoginView, PlaceView, TripView

urlpatterns = [
    path('register', AuthUserRegistrationView.as_view(), name='register'),
    path('login', AuthUserLoginView.as_view(), name='login'),
    path('places', PlaceView.as_view()),
    path('trips', TripView.as_view()),
# r'^update_lab_val/(?P<lab_id>[0-9]+)$'
]