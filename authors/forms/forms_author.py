

#from django.forms import Form, ModelForm 

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.forms_atribute.forms_contet_function import adicionar_attrs, add_placeholder, strong_password


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
        validators=[strong_password],
        widget = forms.PasswordInput(attrs={
            'placeholder':'Repeat your password here'
        })        
    )

    # def clean_password(self):

    #     data = self.cleaned_data.get('password')
        
    #     self.clean_password_2(data)
    #     return data
    
    # def clean_password_2(self, inf, *args):

    #     data = self.cleaned_data.get('password_2')

    #     if data != inf:
    #         raise ValidationError(
    #             'Passwords não são iguais',
    #             code='invalid',                
    #         )
        
    #     return data


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
            },            
        }

        # To have control over the fields

        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'what is your name',
                                                'class':'can insert css'}),
            'password':forms.PasswordInput(attrs={'placeholder':'your password here'}) # To hide the password field
        }
    
    # Here validetes a field 
    # def clean_password(self):
        
    #     data = self.cleaned_data.get('password')

    #     if 'nome' in data:
    #         raise ValidationError(
    #             'Não digite %(var)s',
    #             code='invalid',
    #             params={'var':data}
    #         )           
    #     return data
    

    # Valid email
    def clean_email(self):
        new_email = self.cleaned_data.get('email')

        existi = User.objects.filter(email=new_email)

        if existi:
            raise ValidationError(
                'This email is already in the database',                 
                code='invalid'
            )
        return new_email
    

    # Here validates more of one fields 
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')

        if password != password_2:
            raise ValidationError(
                'Thes field passwords must be equal'                
            )

        