from .models import CustomUser
from django import forms
from django_countries.data import COUNTRIES
from phone_field import PhoneFormField
class UserForm(forms.ModelForm):
    country = forms.ChoiceField(choices = sorted(COUNTRIES.items()), initial = {'Country': 'IN'}, widget=forms.Select(attrs={'style': 'width:150px'}))
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required = True,)
    mobile = PhoneFormField()
    username=forms.CharField()
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name','email', 'mobile', 'country','password']
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username=forms.CharField()
    class Meta:
        model = CustomUser
        fields = ['username', 'password']