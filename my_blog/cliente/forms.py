from django import forms

from cliente.models import Cliente

class ClienteForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del cliente",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cliente-name",
                "placeholder": "Nombre del cliente",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del cliente",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cliente-last-name",
                "placeholder": "Apellido del cliente",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cliente-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Cliente
        fields = ["name", "last_name", "email"]
