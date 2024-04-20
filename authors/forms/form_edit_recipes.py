
from django import forms
from recipes.models import Recipes
from utils.forms_atribute.forms_contet_function import adicionar_attrs
from django.core.exceptions import ValidationError

class FormEditRecipes(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # aula 186 *********
        adicionar_attrs(self.fields.get('preparation_steps'),'class','span-two')
        #adicionar_attrs(self.fields.get('cover'), 'class', 'span-two')


    class Meta:
        model = Recipes

        fields = "title","description","preparation_time",\
                "preparation_time_unit", "serving","serving_unit",\
                "preparation_steps","cover"
        
        widgets = {
            'cover':forms.FileInput(
                attrs={'class':'span-two'}
            ),
            
            'serving_unit':forms.Select(
                choices=(
                    ('horas','Horas'),
                    ('minuto','Minutos')
                )
            ),

            'preparation_time_unit':forms.Select(
                choices=(
                    ('horas','Horas'),
                    ('minutos','Minutos')
                )
            )

        }
    
    def clean_title(self):
        lista = []
        valid_title = self.cleaned_data.get('title')

        for string in valid_title:
            lista.append(string)

        if len(lista) <= 3:
            raise ValidationError(
                'O titulo esta muito pequeno',
                code='invalid',
            )
        return valid_title
    
    def clean_preparation_time(self):
        time = self.cleaned_data.get('preparation_time')

        if time < 0:
            raise ValidationError(
                'O numero não pode ser menor que 0',
                code='invalid',
            )

        return time
    