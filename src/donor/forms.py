from django import forms
from .models import Donar, PoliceStation

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Donar
        fields = ('name', 'mobile_number_1', 'mobile_number_2', 'blood_group','address','distict','police_station')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['police_station'].queryset = PoliceStation.objects.none()
        
        
        if 'distict' in self.data:
            try:
                country_id = int(self.data.get('distict'))
                self.fields['police_station'].queryset = PoliceStation.objects.filter(distict_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['distict'].queryset = self.instance.distict.police_station_set.order_by('name')
