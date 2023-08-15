from django.urls import path
from . import views

urlpatterns = [
    path("", views.news, name="news"),
    path("<int:id>/", views.detail, name="detail"),
    path("create/", views.create_new, name="create_new"),
    path("<int:id>/edit/", views.EditView.as_view(), name="edit")
]