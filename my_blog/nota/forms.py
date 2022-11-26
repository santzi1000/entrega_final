from ckeditor.widgets import CKEditorWidget
from django import forms

from nota.models import Nota
from nota.models import Homework


class NotaForm(forms.ModelForm):
    name = forms.CharField(
        label="titulo del asunto ",
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "nota-name",
                "placeholder": "Asunto",
                "required": "True",
            }
        ),
    )

    code = forms.IntegerField(
        label="Codigo del responsable:",
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "nota-code",
                "placeholder": "Codigo del responsable",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    image = forms.ImageField()

    class Meta:
        model = Nota
        fields = ["name", "code", "description", "image"]


class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )


class HomeworkForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del cliente",
        max_length=80,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "homework-name",
                "placeholder": "Nombre del cliente",
                "required": "True",
            }
        ),
    )

    due_date = forms.DateField(
        label="Cita programada el día:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "homework-code",
                "placeholder": "Fecha yyyy-mm-dd",
                "required": "True",
            }
        ),
    )

    is_delivered = forms.BooleanField(
        label="Cita Confirmada:",
        required=False,
    )

    class Meta:
        model = Homework
        fields = ["name", "due_date", "is_delivered"]
