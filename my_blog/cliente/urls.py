from django.urls import path

from cliente import views

app_name = "cliente"
urlpatterns = [
    path("clientes", views.ClienteListView.as_view(), name="cliente-list"),
    path("cliente/add/", views.ClienteCreateView.as_view(), name="cliente-add"),
    path("cliente/<int:pk>/detail/", views.ClienteDetailView.as_view(), name="cliente-detail"),
    path("cliente/<int:pk>/update/", views.ClienteUpdateView.as_view(), name="cliente-update"),
    path("cliente/<int:pk>/delete/", views.ClienteDeleteView.as_view(), name="cliente-delete"),
]
