from django.urls import path
from .views import costumer_list_create, costumer_detail

urlpatterns = [
    path("costumers/", costumer_list_create),
    path("costumers/<int:pk>/", costumer_detail),
]