#urls.py
from django.urls import path
from library.views import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)

urlpatterns = [
    path('', ListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]
