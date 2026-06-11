

from django import forms
from .models import Booking
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__' #['name', 'email', 'phone', 'date', 'time']
        widgets = {
            'b_date': DateInput(),
            'b_time': TimeInput(),
        }
        labels = {
            'p_name': 'Patient Name',
            'b_date': 'Booking Date',
            'p_phone': 'Phone Number',
            'p_email': 'Email Address',
            'pd_name': 'Doctor',
            'b_time': 'Booking Time'
        }