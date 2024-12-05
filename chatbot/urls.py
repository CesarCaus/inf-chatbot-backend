from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.receive_message, name="receite_message"),
]
