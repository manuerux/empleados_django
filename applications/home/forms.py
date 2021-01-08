from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui',
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
         # TODO Validation
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numnero mayor a 10')

        return cantidad
