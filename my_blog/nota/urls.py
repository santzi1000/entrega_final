from django.urls import path

from nota import views

app_name = "nota"
urlpatterns = [
    path("notas/", views.NotaListView.as_view(), name="nota-list"),
    path("nota/add/", views.NotaCreateView.as_view(), name="nota-add"),
    path("nota/<int:pk>/detail/", views.NotaDetailView.as_view(), name="nota-detail"),
    path("nota/<int:pk>/update/", views.NotaUpdateView.as_view(), name="nota-update"),
    path("nota/<int:pk>/delete/", views.NotaDeleteView.as_view(), name="nota-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),

    path("homeworks", views.HomeworkListView.as_view(), name="homework-list"),
    path("homework/add/", views.HomeworkCreateView.as_view(), name="homework-add"),
    path("homework/<int:pk>/detail/", views.HomeworkDetailView.as_view(), name="homework-detail"),
    path("homework/<int:pk>/update/", views.HomeworkUpdateView.as_view(), name="homework-update"),
    path("homework/<int:pk>/delete/", views.HomeworkDeleteView.as_view(), name="homework-delete"),
]
