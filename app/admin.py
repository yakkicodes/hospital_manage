
from django.contrib import admin
from .models import Booking, Departments, Members

class BookingAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'pd_name', 'b_date', 'b_time', 'on_b', 'on_t','p_email','p_phone')
    list_filter = ('b_date', 'pd_name__m_department')
    search_fields = ('p_name', 'pd_name__m_name')


admin.site.register(Departments)
admin.site.register(Members)
admin.site.register(Booking, BookingAdmin)


    