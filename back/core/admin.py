from django.contrib import admin

# Register your models here.
from core.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('date', 'trainer', 'location', 'name',
                    'surname', 'phone', 'amount',
                    'payment_type', 'payment_date')


admin.site.register(Payment, PaymentAdmin)
