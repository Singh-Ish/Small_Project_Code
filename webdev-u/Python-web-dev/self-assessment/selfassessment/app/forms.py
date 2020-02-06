from django import forms
from django.core import validators
from app.models import User




class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    #botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email =all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email !=vmail:
            raise forms.ValidationError("Make sure your email match!")

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'
