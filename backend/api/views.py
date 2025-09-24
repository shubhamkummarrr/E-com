from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import costumer
from .serializers import CostumerSerializer, RegisterSerializer, MeSerializer
from rest_framework.views import APIView 
from rest_framework import permissions   


class RegisterView(APIView):
    """POST /api/auth/register/"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # serializer handles set_password
        return Response(MeSerializer(user).data, status=status.HTTP_201_CREATED)


class MeView(APIView):
    """GET /api/users/me/"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(MeSerializer(request.user).data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def costumer_list_create(request):
    if request.method == "GET":
        qs = costumer.objects.all()
        return Response(CostumerSerializer(qs, many=True).data)

    # POST
    ser = CostumerSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def costumer_detail(request, pk):
    obj = get_object_or_404(costumer, pk=pk)

    if request.method == "GET":
        return Response(CostumerSerializer(obj).data)

    if request.method == "PUT":
        ser = CostumerSerializer(obj, data=request.data)
    elif request.method == "PATCH":
        ser = CostumerSerializer(obj, data=request.data, partial=True)
    elif request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)