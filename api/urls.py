from django.contrib import admin
from django.urls import path, include
from .views import (
    AddressFindAPIView,
    AddressRetrieveAPIView,
)

urlpatterns = [
    path('find/',AddressFindAPIView.as_view(),name='find'),
    path('retrieve/',AddressRetrieveAPIView.as_view(),name='retrieve'),
]