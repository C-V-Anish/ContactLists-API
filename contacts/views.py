from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from rest_framework import permissions
# Create your views here.

class ContactLC(ListCreateAPIView):
    serializer_class=ContactSerializer
    permission_classes=(permissions.IsAuthenticated)

    def get_queryset(self):
        return super().get_queryset()
    
    def perform_create(self, serializer):
        serializer.save()



class ContactRUD(RetrieveUpdateDestroyAPIView):
    serializer_class=ContactSerializer
    permission_classes=(permissions.IsAuthenticated)