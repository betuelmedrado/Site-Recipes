
#from django.forms import Form, ModelForm 

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# ========== AULA 135  (Uderm) 
# function to insert values into the field attrs
def adicionar_attrs(field, attrs_name,attrs_new_val):
    existing_attr = field.widget.attrs.get(attrs_name,'')
    field.widget.attrs[attrs_name] = f'{existing_attr} {attrs_new_val}'.strip()

def add_placeholder(fields, placeholder_val):
    adicionar_attrs(fields,'placeholder', placeholder_val)


class RegisterForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # using the "adicionar_attrs" function
        adicionar_attrs(self.fields['last_name'],'placeholder','Seu segundo nome')
        adicionar_attrs(self.fields['email'], 'placeholder', 'Um e-mail valido')


    # I gol put other password field 
    #I can do it like this.
    # creat the field "password_2"
    password_2 = forms.CharField(
        required=True,
        help_text='Repeat your password here',
        widget = forms.PasswordInput(attrs={
            'placeholder':'Repeat your password here'
        })
    )

    def clean_password(self):

        data = self.cleaned_data.get('password')
        
        self.clean_password(data)
        return data
    
    def clean_password_2(self, inf):

        data = cleaned_data.get('password_2')

        if datas != inf:
            raise ValidationError(
                'Passwords não são iguais',
                code='invalid',                
            )
        
        return datas


    # Can I use the default "Meta" class
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','password']

        # labels dos campos 
        labels = {'first_name':'Nome','last_name' :'Sobrenome', 'email':'e-mail'}

        # field help text

        help_texts = {
            'password':'Your password must contain, uppercase letters and at leats two number',
            'email':'this field must be valid'
        }

        error_messages = {
            'username' : {
                'required':' this field not must be empty', 
                'max_length':'This field must have less than 3 charact'
            },
            'first_name':{
                'required':'This field not must be empty'
            }
        }

        # To have control over the fields

        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'what is your name',
                                                'class':'can insert css'}),
            'password':forms.PasswordInput(attrs={'placeholder':'your password here'}) # To hide the password field
        }
