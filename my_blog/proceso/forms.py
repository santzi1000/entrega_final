from django import forms

from proceso.models import Proceso

class ProcesoForm(forms.ModelForm):
    name = forms.CharField(
        label="Juzgado donde recide",
        max_length=80,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "proceso-name",
                "placeholder": "Juzgado",
                "required": "True",
            }
        ),
    )
    tipe = forms.CharField(
        label="Tipo de proceso",
        max_length=60,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "proceso-tipe",
                "placeholder": "Tipo de Proceso",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email del despacho:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "proceso-email",
                "placeholder": "email del juzgado",
                "required": "True",
            }
        ),
    )
    radicado = forms.CharField(
        label="Radicado:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "proceso-radicado",
                "placeholder": "radicado",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Proceso
        fields = ["name", "tipe", "email", "radicado"]
