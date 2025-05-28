from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core.exceptions import ValidationError

from Accounts.models import CustomUserModel

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'input-field',
        'placeholder': 'Ваш email'
    }))
    
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-field'})
        self.fields['password1'].widget.attrs.update({'class': 'input-field'})
        self.fields['password2'].widget.attrs.update({'class': 'input-field'})
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUserModel.objects.filter(email=email).exists():
            raise ValidationError("Этот email уже используется")
        return email

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-field'})
        self.fields['password'].widget.attrs.update({'class': 'input-field'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email', 'first_name', 'last_name')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input-field'})