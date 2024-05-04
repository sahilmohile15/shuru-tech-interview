from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('store-match/', StoreMatchesView.as_view(), name='Store-Match' ),
    path('get-matches/', RetrieveMatchByDateView.as_view(), name='Retrieve-Match')
]
