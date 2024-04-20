
from django import forms

from utils.forms_atribute.forms_contet_function import add_placeholder, adicionar_attrs, strong_password


class Login(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        add_placeholder(self.fields['username'], 'your user name')
#        add_placeholder(self.fields['password'], 'you password!')        
 #       strong_password(self.fields['email'])


    username = forms.CharField(max_length=50)
    #email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    