from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(LaundryService)
admin.site.register(Booking)
admin.site.register(ContactMessage)
admin.site.register(Review)