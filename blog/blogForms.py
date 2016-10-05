from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Usuario, Mamadas

class userForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {
        	'nombre': _(''),
        }
        widgets = {
        	'nombre': forms.TextInput(attrs =
        		{
        			'type': 'text',
        			'placeholder': 'nombre'
        		}),
        }
    
class datosForm(forms.ModelForm):
    class Meta:
        model = Mamadas
        fields = ('telefono','direccion')
    
