from django.urls import path
from .views import costumer_list_create, costumer_detail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, MeView


urlpatterns = [
    path("costumers/", costumer_list_create),
    path("costumers/<int:pk>/", costumer_detail),
    # Auth
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="jwt-login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    
    # User
    path("users/me/", MeView.as_view(), name="me"),


]