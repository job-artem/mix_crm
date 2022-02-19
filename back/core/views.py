from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from core.models import Payment, Attendance
from core.serializers import PaymentSerializer, AttendanceSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    lookup_field = 'trainer'


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    lookup_field = 'trainer'
