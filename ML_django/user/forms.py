from .models import CustomUser
from django import forms
from django_countries.data import COUNTRIES
class UserForm(forms.ModelForm):
    country = forms.ChoiceField(choices = sorted(COUNTRIES.items()), initial = {'Country': 'IN'})
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required = True)
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