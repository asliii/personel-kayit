from django import forms
from .models import Personel

Gender_Chocies= [
    ('Woman', 'Kadın'),
    ('Man', 'Erkek'),
    ]

class PostForm(forms.ModelForm):
    fullName=forms.CharField(label='Tam Adı ',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'orn: Aslıhan Çetin'
        }
    ))
    email = forms.CharField(label='Eposta ',widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'xxx@xx.xx'
        }
    ))
    facebook = forms.CharField(label='Facebook Adresi ', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'https://facebook.com'
        }
    ))
    twitter = forms.CharField(label='Twitter Adresi ', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'https://twitter.com'
        }
    ))
    phone = forms.CharField(label='Telefon ',widget=forms.TextInput(
        attrs={
            'class': 'form-control phone_us',
            'placeholder': '(xxx)-xx-xxxx'
        }
    ))
    
    gender = forms.CharField(label='Cinsiyet ', widget=forms.Select(choices=Gender_Chocies, attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = Personel
        fields = ('fullName', 'email','phone','position','gender','facebook','twitter')
