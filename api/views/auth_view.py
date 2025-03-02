from django.http import HttpResponse
from rest_framework import generics
from api.models.user_model import CustomUser
from api.serializers.auth_view_serializer import UserSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class RegisterUser(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Calls UserSerializer.create()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)