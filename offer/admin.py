from django.contrib import admin

from offer.models import Offer


# Register your models here.
class OfferAdmin(admin.ModelAdmin):
    list_display = ('company', 'url', 'application_date', 'status', 'last_interview_date', 'result')


admin.site.register(Offer, OfferAdmin)
