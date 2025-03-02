from django.http import HttpResponse
from rest_framework import generics
from api.models.user_model import CustomUser
from api.serializers.auth_view_serializer import UserSerializer, UserLoginSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class UserRegisterView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Calls UserSerializer.create()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({'Message':'Login Successfull'}, status=status.HTTP_200_OK)
            else:
                return Response({'Errors':{'Non Field Errors' : ['Email or password is Incorrect']}}, status=status.HTTP_404_NOT_FOUND)   
    