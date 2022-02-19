from rest_framework import serializers

from core.models import Payment, Attendance


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ("date", "trainer", "location", "name", "surname",
                  "phone", "amount", "payment_type", "payment_date")
        lookup_field = 'trainer'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ("date", "trainer", "location", "time", "day",
                  "all_count", "first_count", "abonement_count")
        lookup_field = 'trainer'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }