from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from cliente.models import Cliente
from cliente.forms import ClienteForm


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 3


class ClienteDetailView(DetailView):
    model = Cliente
    fields = ["name", "last_name", "email"]


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    success_url = reverse_lazy("cliente:cliente-list")

    form_class = ClienteForm

    def form_valid(self, form):
        """Filter to avoid duplicate clientes"""
        data = form.cleaned_data
        actual_objects = Cliente.objects.filter(
            name=data["name"],
            last_name=data["last_name"],
            email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El Cliente {data['name']} {data['last_name']} | {data['email']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Cliente: {data['name']} - {data['last_name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["name", "last_name", "email"]

    def get_success_url(self):
        cliente_id = self.kwargs["pk"]
        return reverse_lazy("cliente:cliente-detail", kwargs={"pk": cliente_id})


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("cliente:cliente-list")
