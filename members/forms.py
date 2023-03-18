from django import forms 
from .models import Member

class memberform(forms.ModelForm): 
    class Meta: 
        model = Member
        fields = '__all__'
        labels = {'first_name': 'First Name'
                  , 'last_name': 'Last Name'
                  , 'email': 'Email'
                  , 'phone_number': 'Phone Number'
                  , 'hop': 'HOP'
                  , 'date_joined' : 'Date Joined'
                  , 'occupation' : 'Occupation'
                  , 'extra_notes' : 'Extra Notes'

                  }
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'})
                  , 'last_name': forms.TextInput(attrs={'class': 'form-control'})
                  , 'email': forms.EmailInput(attrs={'class': 'form-control'})
                  , 'phone_number': forms.NumberInput(attrs={'class': 'form-control'})
                  , 'hop': forms.TextInput(attrs={'class': 'form-control'})
                  , 'date_joined': forms.DateInput(attrs={'class': 'form-control'})
                  , 'occupation': forms.TextInput(attrs={'class': 'form-control'})
                  , 'extra_notes': forms.Textarea(attrs={'class': 'form-control'})
                  }
        