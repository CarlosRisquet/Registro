from django import forms
from .models import Pedido,Producto,Municipio, Tipo_Venta, Articulo


class ProductoForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Piezaform."""

        model = Producto
        fields = ('pedido','articulo','cantidad','tipo','precio_tienda','import_fact')
        widgets = {
            'pedido': forms.TextInput(
            attrs= {
                'class':'form-control'
            } 
            ),
            'articulo':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'cantidad': forms.TextInput(
            attrs= {
                'class':'form-control'
            } 
            ),
            'tipo': forms.Select(
            attrs= {
                'class':'form-control'
            } 
            ),
            'precio_tienda': forms.TextInput(
            attrs= {
                'class':'form-control'
            } 
            ),
            'import_fact': forms.TextInput(
            attrs= {
                'class':'form-control'
            } 
            ),

        }

class ArticuloForm(forms.ModelForm):
    """Form definition for Arti."""

    class Meta:
        """Meta definition for Artiform."""

        model = Articulo
        fields = ('codigo','nombre')
        widgets = {
            'codigo': forms.TextInput(
            attrs= {
                'class':'form-control'
            } 
            ),
            'nombre':forms.TextInput(
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


class PedidoForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Pedido
        fields = ('numero','municipio','fecha_compra','orden_trabajo','pre_fact','fact','fecha','entregado','recibe')
        widgets = {
            'numero':forms.TextInput(
                attrs = {
                    'class':'form-control'

                }
            ),
            'municipio':forms.Select(
                attrs = {
                    'class':'form-control'

                }
            ),
            'fecha_compra':forms.DateTimeInput(
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
            'fecha':forms.DateTimeInput(
                attrs = {
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
            )
        }
