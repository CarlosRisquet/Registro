from django import forms
from .models import Almacen

class AlmacenForm(forms.ModelForm):
    """Form definition for Ar."""

    class Meta:
        """Meta definition for Arform."""

        model = Almacen
        fields = ('articulo','cantidad','imagen')
        widgets = {
            'articulo': forms.Select(
            attrs= {
                'class':'form-control'
            }
            ),
            'cantidad': forms.TextInput(
            attrs= {
                'class':'form-control'
            } 
            ),
            'imagen': forms.ImageField(
                attrs={
                    'class':'form-control'
                }
            ),
}