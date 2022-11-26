from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from proceso.models import Proceso
from proceso.forms import ProcesoForm


class ProcesoListView(ListView):
    model = Proceso
    paginate_by = 3


class ProcesoDetailView(DetailView):
    model = Proceso
    fields = ["name", "tipe", "email", "radicado"]


class ProcesoCreateView(LoginRequiredMixin, CreateView):
    model = Proceso
    success_url = reverse_lazy("proceso:proceso-list")

    form_class = ProcesoForm

    def form_valid(self, form):
        """Filter to avoid duplicate procesos"""
        data = form.cleaned_data
        actual_objects = Proceso.objects.filter(
            name=data["name"],
            tipe=data["tipe"],
            email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El Proceso {data['name']} {data['tipe']} | {data['email']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Proceso: {data['name']} - {data['tipe']}. Creado exitosamente!", #cambiar validacion para el radicado
            )
            return super().form_valid(form)


class ProcesoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proceso
    fields = ["name", "tipe", "email", "radicado"]

    def get_success_url(self):
        proceso_id = self.kwargs["pk"]
        return reverse_lazy("proceso:proceso-detail", kwargs={"pk": proceso_id})


class ProcesoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proceso
    success_url = reverse_lazy("proceso:proceso-list")
