from django import forms
from .models import Registro,Pieza,Municipio, Tipo_Venta


class PiezaForm(forms.ModelForm):
    """Form definition for Pieza."""

    class Meta:
        """Meta definition for Piezaform."""

        model = Pieza
        fields = ('pieza','codigo')
        widgets = {
            'pieza': forms.TextInput(
            attrs= {
                'class':'form-control'
            } 
            ),
            'codigo':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),

        }

class MunicipioForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Municipio
        fields = ('municipio',)
        widgets = {
            'municipio':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
           }
        
class Tipo_VentaForm(forms.ModelForm):
    """Form definition for Tipo_Venta."""

    class Meta:
        """Meta definition for Tipo_Ventaform."""

        model = Tipo_Venta
        fields = ('tipo',)
        widgets = {
            'tipo':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
           }


class RegistroForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Registro
        fields = ('pedido','fecha_compra','municipio','pieza','tipo','cantidad','precio_tienda','import_fact','orden_trabajo','pre_fact','fact','entregado','recibe','fecha')
        widgets = {
            'pedido':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'fecha_compra':forms.DateTimeInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'municipio':forms.Select(
                attrs = {
                    'class':'form-control'

                }
            ),
            'pieza':forms.Select(
                attrs = {
                    'class':'form-control'

                }
            ),
            'tipo':forms.Select(
                attrs = {
                    'class':'form-control'

                }
            ),
            'cantidad':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'precio_tienda':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'import_fact':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'orden_trabajo':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'pre_fact':forms.TextInput(
                attrs = {
                    'required': False,
                    'class':'form-control'

                }
            ),
            'fact':forms.TextInput(
                attrs = {
                    'required': False,
                    'class':'form-control'

                }
            ),
            'entregado':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'recibe':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'fecha':forms.DateTimeInput(
                attrs = {
                    'class':'form-control'

                }
            ),
        }
