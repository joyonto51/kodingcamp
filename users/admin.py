from django.contrib import admin

from .models import PersonalProfile, OrganizationProfile

admin.site.register(PersonalProfile)
admin.site.register(OrganizationProfile)
