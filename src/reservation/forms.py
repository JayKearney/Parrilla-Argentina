from django import forms
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        # name = forms.CharField(required=True)
        # email = forms.EmailField(required=True)
        # phone = forms.CharField(required=True)
        # number_of_person = forms.CharField(required=True)
        # Date = forms.DateField(required=True)
        # time = forms.TimeField(required=True)