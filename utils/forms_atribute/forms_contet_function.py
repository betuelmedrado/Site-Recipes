


from django.core.exceptions import ValidationError

# import regular expression
import re


# ========== AULA 135  (Uderm) 
# function to insert values into the field attrs
def adicionar_attrs(field, attrs_name,attrs_new_val):
    existing_attr = field.widget.attrs.get(attrs_name,'')
    field.widget.attrs[attrs_name] = f'{existing_attr} {attrs_new_val}'.strip()



# This I did for testing 
#def addcionar_attr_test(field, nome_attr, attr_novo_valor):    
 #   campo = field.widget.attrs.get(nome_attr)
  #  field.widget.attrs[nome_attr] = attr_novo_valor


def add_placeholder(fields, placeholder_val):
    adicionar_attrs(fields,'placeholder', placeholder_val)

    

# function to validates the fields using  regular expression 
def strong_password(may_password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[1-9]).{8,}')    

    if not regex.match(may_password):
        raise ValidationError(
            'Your password must contain, uppercase letters and at leats 8 number',
            code='Invalid'
        )