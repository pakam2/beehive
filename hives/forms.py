from django import forms
from django.forms import ModelForm
from hives.models import HiveModel, FirstHiveDataModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class AddHiveForm(ModelForm):
    class Meta:
        model = HiveModel
        fields = '__all__'

    #Making the 'max' value of the field equal to 1
    def __init__(self, *args, **kwargs):
        super(AddHiveForm,self).__init__(*args, **kwargs)
        self.fields['numberOfHive'].widget = forms.NumberInput(attrs={'step':1, 'min':1})


class HiveDataForm(ModelForm):

    class Meta:
        model = FirstHiveDataModel
        exclude = ['hive']


    #Making the 'max' value of the fileds equal to 1
    def __init__(self, *args, **kwargs):
        super(HiveDataForm, self).__init__(*args, **kwargs)
        self.fields['first_frame_honey'].widget = forms.NumberInput(attrs={'class':'slider', 'type':'range', min:1, 'max': 100, 'id': 'first_frame_honey', 'value': 50})
        self.fields['first_frame_speck'].widget = forms.NumberInput(attrs={'class':'slider','type':'range', min:1, 'max': 100, 'id': 'first_frame_speck', 'value': 50})
        self.fields['first_frame_beebread'].widget = forms.NumberInput(attrs={'class':'slider','type':'range', min:1, 'max': 100,'id': 'first_frame_beebread', 'value': 50})
        self.fields['first_frame_worm'].widget = forms.NumberInput(attrs={'class':'slider','type':'range', min:1, 'max': 100, 'id': 'first_frame_worm', 'value': 50})

        self.fields['second_frame_honey'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['second_frame_speck'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['second_frame_beebread'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['second_frame_worm'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})

        self.fields['third_frame_honey'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['third_frame_speck'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['third_frame_beebread'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['third_frame_worm'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})

        self.fields['fourth_frame_honey'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['fourth_frame_speck'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['fourth_frame_beebread'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['fourth_frame_worm'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})

        self.fields['fifth_frame_honey'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['fifth_frame_speck'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['fifth_frame_beebread'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['fifth_frame_worm'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})

        self.fields['sixth_frame_honey'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['sixth_frame_speck'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['sixth_frame_beebread'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['sixth_frame_worm'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
class SignInForm(forms.Form):

    login = forms.CharField(label="Login" ,widget=forms.TextInput(attrs={'class' : 'inputField', 'placeholder' : 'Twój login', 'autocomplete' : 'nope'}))
    password = forms.CharField(label="Hasło" ,widget=forms.PasswordInput(attrs={'class': 'inputField', 'placeholder' : 'Twoje hasło', 'autocomplete' : 'nope'}))

class MySignUpForm(UserCreationForm):
        first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        email = forms.EmailField(max_length=254)
        password1 = forms.CharField(widget=forms.PasswordInput(), help_text='')
        class Meta:
            model = User
            fields = ('username', 'last_name', 'password1', 'password2', )
