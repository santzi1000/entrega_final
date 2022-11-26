from django.urls import path

from proceso import views

app_name = "proceso"
urlpatterns = [
    path("procesos", views.ProcesoListView.as_view(), name="proceso-list"),
    path("proceso/add/", views.ProcesoCreateView.as_view(), name="proceso-add"),
    path("proceso/<int:pk>/detail/", views.ProcesoDetailView.as_view(), name="proceso-detail"),
    path("proceso/<int:pk>/update/", views.ProcesoUpdateView.as_view(), name="proceso-update"),
    path("proceso/<int:pk>/delete/", views.ProcesoDeleteView.as_view(), name="proceso-delete"),
]
