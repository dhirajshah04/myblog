from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.contrib.auth.models import User

#User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This User does not Exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")

            if not user.is_active:
                raise forms.ValidationError("This user is not active")

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']