from django import forms

class FormularioCliente(forms.Form):
    nombre = forms.DateField()
    direccion = forms.DateField()
    email = forms.EmailField()
    celular = forms.DateField()


class Ventrega(forms.Form):
    N_pedido = forms.IntegerField()

