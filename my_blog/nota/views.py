from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from nota.forms import CommentForm
from nota.forms import NotaForm
from nota.forms import HomeworkForm
from nota.models import Comment
from nota.models import Nota
from nota.models import Homework


class NotaListView(ListView):
    model = Nota
    paginate_by = 3


class NotaDetailView(DetailView):
    model = Nota
    template_name = "nota/nota_detail.html"
    fields = ["name", "code", "description"]

    def get(self, request, pk):
        nota = Nota.objects.get(id=pk)
        comments = Comment.objects.filter(nota=nota).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "nota": nota,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class NotaCreateView(LoginRequiredMixin, CreateView):
    model = Nota
    success_url = reverse_lazy("nota:nota-list")

    form_class = NotaForm
    # fields = ["name", "code", "description", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate notas"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Nota.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El nota {data['name']} - {data['code']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Nota {data['name']} - {data['code']} creado exitosamente!",
            )
            return super().form_valid(form)


class NotaUpdateView(LoginRequiredMixin, UpdateView):
    model = Nota
    fields = ["name", "code", "description", "image"]

    def get_success_url(self):
        nota_id = self.kwargs["pk"]
        return reverse_lazy("nota:nota-detail", kwargs={"pk": nota_id})

    def post(self):
        pass


class NotaDeleteView(LoginRequiredMixin, DeleteView):
    model = Nota
    success_url = reverse_lazy("nota:nota-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        nota = get_object_or_404(Nota, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, nota=nota
        )
        comment.save()
        return redirect(reverse("nota:nota-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        nota = self.object.nota
        return reverse("nota:nota-detail", kwargs={"pk": nota.id})


class HomeworkListView(ListView):
    model = Homework
    paginate_by = 4


class HomeworkCreateView(LoginRequiredMixin, CreateView):
    model = Homework
    success_url = reverse_lazy("nota:homework-list")

    form_class = HomeworkForm

    def form_valid(self, form):
        """Filter to avoid duplicate homeworks"""
        data = form.cleaned_data
        actual_objects = Homework.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El cita {data['name']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Cita: {data['name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class HomeworkDetailView(DetailView):
    model = Homework
    fields = ["name", "due_date", "is_delivered"]


class HomeworkUpdateView(LoginRequiredMixin, UpdateView):
    model = Homework
    fields = ["name", "due_date", "is_delivered"]

    def get_success_url(self):
        homework_id = self.kwargs["pk"]
        return reverse_lazy("nota:homework-detail", kwargs={"pk": homework_id})


class HomeworkDeleteView(LoginRequiredMixin, DeleteView):
    model = Homework
    success_url = reverse_lazy("nota:homework-list")
