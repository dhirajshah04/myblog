from django import forms
from .models import Post
from django.core import validators

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
                  'image',
                  'text',
                  )

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control txtinput', 'placeholder':'Enter Your Name',

        }
    ))
    Email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(
        attrs={
            'class':'form-control','placeholder': 'Enter Your Email',
        }
    ))
    Message = forms.CharField(
        max_length=2000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'class':'form-control','placeholder':'Enter Your Message',
            }
        )
    )
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty", validators=[validators.MaxLengthValidator(0)])